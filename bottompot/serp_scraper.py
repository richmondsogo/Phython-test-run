import asyncio
import random
from pathlib import Path
from loguru import logger
from playwright.async_api import async_playwright, Page, Browser, BrowserContext

from config import (
    MAX_PAGES,
    PAGE_LOAD_TIMEOUT,
    ELEMENT_TIMEOUT,
    DELAY_MIN,
    DELAY_MAX,
)
from models import ATSConfig, RawSearchResult, SearchParams
from query_builder import MultiATSQueryBuilder, QueryBuilder

DEBUG_DIR = Path("debug_dumps")


async def _random_delay(min_s: float = DELAY_MIN, max_s: float = DELAY_MAX) -> None:
    """Mimics human think-time between actions."""
    await asyncio.sleep(random.uniform(min_s, max_s))


async def _build_stealth_context(browser: Browser) -> BrowserContext:
    """
    Creates a browser context that reduces fingerprinting surface.
    Not bulletproof — Google's detection is sophisticated — but handles
    the basic checks: consistent UA, realistic viewport, no webdriver flag.
    """
    context = await browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        ),
        viewport={"width": 1366, "height": 768},
        locale="en-US",
        timezone_id="America/New_York",
        # Tells the browser to report a real colour depth / pixel ratio
        device_scale_factor=1.0,
        java_script_enabled=True,
    )

    # Mask navigator.webdriver — the most common bot signal
    await context.add_init_script(
        """
        Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
        Object.defineProperty(navigator, 'plugins', { get: () => [1, 2, 3] });
    """
    )

    return context


async def _parse_serp_results(
    page: Page, ats: ATSConfig, query_str: str
) -> list[RawSearchResult]:
    """
    Extracts job listing URLs from a Google SERP page.

    Google's DOM isn't stable — they A/B test layouts constantly.
    We use a layered selector strategy: preferred → fallback → last resort.
    """
    results: list[RawSearchResult] = []

    # Check for CAPTCHA before attempting to parse
    if await _is_captcha_page(page):
        await _dump_page(page, f"CAPTCHA_{ats.name}")
        raise RuntimeError(
            f"CAPTCHA triggered on {ats.label}. "
            "Session is burned — check debug_dumps/captcha_*.png. "
            "Wait 30–60 min before retrying, or rotate IP."
        )

    # Current Google DOM (verified March 2026):
    # Each organic result lives in a div.tF2Cxc
    result_containers = await page.query_selector_all("div.tF2Cxc")

    # Fallback: older layout still uses div.g in some regions/experiments
    if not result_containers:
        result_containers = await page.query_selector_all("div.g")

    if not result_containers:
        logger.warning(
            f"No result containers found for {ats.label} — dumping page for inspection."
        )
        await _dump_page(page, ats.name)
        return results

    for container in result_containers:
        try:
            # Primary link lives in a.zReHs in the current layout
            link_el = await container.query_selector("a.zReHs")
            if not link_el:
                # Fallback to any href if the class changes
                link_el = await container.query_selector("a[href]")
            if not link_el:
                continue

            href = await link_el.get_attribute("href")
            if not href or not href.startswith("http"):
                continue

            # Filter out Google's own URLs that leak into results
            if "google.com" in href or "webcache" in href:
                continue

            # Must actually contain the ATS domain we queried for
            if ats.site_operator not in href:
                continue

            # Title is in h3.LC20lb
            h3 = await container.query_selector("h3.LC20lb")
            if not h3:
                h3 = await container.query_selector("h3")
            title = (await h3.inner_text()).strip() if h3 else href

            # Snippet is in div.VwiC3b
            snippet_el = await container.query_selector("div.VwiC3b")
            snippet = (await snippet_el.inner_text()).strip() if snippet_el else None

            results.append(
                RawSearchResult(
                    url=href,
                    title=title,
                    snippet=snippet,
                    ats_source=ats.name,
                    query_used=query_str,
                )
            )

        except Exception as e:
            logger.debug(f"Skipped a result container: {e}")
            continue

    return results


async def _dump_page(page: Page, label: str) -> None:
    """
    Saves a screenshot + raw HTML of the current page to debug_dumps/.
    Run this once to inspect what Google is actually returning.
    The HTML will show you what selectors are real in the current layout.
    """
    DEBUG_DIR.mkdir(exist_ok=True)
    slug = label.replace(" ", "_").lower()
    screenshot_path = DEBUG_DIR / f"{slug}.png"
    html_path = DEBUG_DIR / f"{slug}.html"

    await page.screenshot(path=str(screenshot_path), full_page=True)
    html = await page.content()
    html_path.write_text(html, encoding="utf-8")

    logger.info(f"Debug dump saved → {screenshot_path} + {html_path}")


async def _is_captcha_page(page: Page) -> bool:
    """Detects Google's reCAPTCHA and 'unusual traffic' pages."""
    content = await page.content()
    signals = ["recaptcha", "unusual traffic", "captcha", "/sorry/"]
    return any(s in content.lower() for s in signals)


async def _scrape_ats_platform(
    context: BrowserContext,
    ats: ATSConfig,
    params: SearchParams,
    max_pages: int = MAX_PAGES,
) -> list[RawSearchResult]:
    """
    Runs the full scrape for a single ATS platform: iterates pages,
    parses results, respects delays.
    """
    all_results: list[RawSearchResult] = []
    builder = QueryBuilder(ats)
    query_str = builder.build_query_string(params)

    page = await context.new_page()

    try:
        for page_num in range(max_pages):
            url = builder.build_url(params, page=page_num)
            logger.info(f"[{ats.label}] Page {page_num + 1} → {url}")

            await page.goto(
                url, wait_until="domcontentloaded", timeout=PAGE_LOAD_TIMEOUT
            )
            await _random_delay()  # let JS settle + looks human

            page_results = await _parse_serp_results(page, ats, query_str)
            logger.info(
                f"[{ats.label}] Page {page_num + 1}: {len(page_results)} results"
            )

            all_results.extend(page_results)

            # If Google returned fewer results than a full page, we've hit the end
            if len(page_results) < 8:
                logger.info(f"[{ats.label}] Sparse results — stopping pagination early")
                break

            # Delay between pages — critical for avoiding rate limits
            await _random_delay(min_s=2.5, max_s=5.0)

    except RuntimeError as e:
        # CAPTCHA — propagate up so the whole run halts, not just this platform
        raise
    except Exception as e:
        logger.error(f"[{ats.label}] Scrape failed: {e}")
    finally:
        await page.close()

    return all_results


class SERPScraper:
    """
    Orchestrates Google SERP scraping across all ATS platforms.

    Usage:
        scraper = SERPScraper()
        results = await scraper.run(SearchParams(job_title="Data Engineer", remote=True))
    """

    def __init__(self, headless: bool = True):
        self.headless = headless  # set False to watch/debug in real browser

    async def run(self, params: SearchParams, platforms=None) -> list[RawSearchResult]:
        all_results: list[RawSearchResult] = []

        async with async_playwright() as pw:
            browser = await pw.chromium.launch(
                headless=self.headless,
                args=[
                    "--disable-blink-features=AutomationControlled",
                    "--no-sandbox",
                    "--disable-dev-shm-usage",  # important inside Docker
                ],
            )
            context = await _build_stealth_context(browser)

            multi_builder = (
                MultiATSQueryBuilder(platforms=platforms)
                if platforms
                else MultiATSQueryBuilder()
            )
            platform_queries = multi_builder.build_all(params)

            for ats, query_str, _ in platform_queries:
                logger.info(f"Starting scrape: {ats.label} | Query: {query_str}")
                try:
                    results = await _scrape_ats_platform(context, ats, params)
                    all_results.extend(results)
                except RuntimeError as e:
                    logger.error(str(e))
                    logger.warning(
                        "Halting run — CAPTCHA triggered. Fix stealth before retrying."
                    )
                    break

                # Delay between ATS platforms — different domains but same IP
                await _random_delay(min_s=3.0, max_s=7.0)

            await browser.close()

        logger.success(f"Total results collected: {len(all_results)}")
        return all_results
