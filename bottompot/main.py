import asyncio
from loguru import logger

from config import ATS_PLATFORMS
from models import SearchParams
from serp_scraper import SERPScraper


async def main():
    params = SearchParams(
        job_title="python intern",
        remote=True,
        days_back=7,
    )

    # DEBUG MODE: run only Greenhouse until selectors are confirmed working.
    # Comment this out and pass nothing to scraper.run() to use all platforms.
    debug_platforms = [p for p in ATS_PLATFORMS if p.name == "greenhouse"]

    logger.info(
        f"Starting Bottom Pot | Job: '{params.job_title}' | Platforms: {[p.label for p in debug_platforms]}"
    )

    # headless=False — watch the browser, check what Google actually renders
    scraper = SERPScraper(headless=False)
    results = await scraper.run(params, platforms=debug_platforms)

    for r in results:
        print(f"\n[{r.ats_source.upper()}] {r.title}")
        print(f"  URL: {r.url}")
        if r.snippet:
            print(f"  Snippet: {r.snippet[:120]}...")

    print(f"\n{'='*60}")
    print(f"Total results: {len(results)}")
    print(
        "\nCheck debug_dumps/ if you got 0 results — the HTML will show the real selectors."
    )


if __name__ == "__main__":
    asyncio.run(main())
