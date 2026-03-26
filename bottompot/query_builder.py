from datetime import datetime, timedelta
from urllib.parse import urlencode

from config import ATS_PLATFORMS, GOOGLE_BASE_URL
from models import ATSConfig, SearchParams


class QueryBuilder:
    """
    Builds parameterised Google search queries that target ATS platforms directly.

    Query anatomy:
        site:{ats_operator} "{job_title}" "remote" after:{YYYY-MM-DD}

    The site: operator locks Google to a single ATS domain.
    Quoted strings force exact matches — reduces noise significantly.
    after: keeps results within your freshness window.
    """

    def __init__(self, ats: ATSConfig):
        self.ats = ats

    def build_query_string(self, params: SearchParams) -> str:
        """Returns the raw query string sent to Google's q= parameter."""
        parts = [f"site:{self.ats.site_operator}"]

        # Wrap multi-word titles in quotes; single words don't need it
        title = params.job_title.strip()
        parts.append(f'"{title}"' if " " in title else title)

        if params.remote:
            parts.append('"remote"')

        date_threshold = (datetime.utcnow() - timedelta(days=params.days_back)).strftime("%Y-%m-%d")
        parts.append(f"after:{date_threshold}")

        return " ".join(parts)

    def build_url(self, params: SearchParams, page: int = 0) -> str:
        """
        Returns a full Google search URL.

        page: 0-indexed. Google paginates with start=0, 10, 20...
        tbs=qdr:w is a secondary freshness filter (past week) — belt and braces
        alongside the after: operator.
        """
        query_string = self.build_query_string(params)
        url_params = {
            "q": query_string,
            "tbs": self._tbs_from_days(params.days_back),
            "start": page * 10,
            "num": 10,
        }
        return f"{GOOGLE_BASE_URL}?{urlencode(url_params)}"

    def _tbs_from_days(self, days_back: int) -> str:
        """
        Maps days_back to Google's tbs (time-based search) parameter.
        Redundant with after: but Google can ignore after: — tbs is more reliable.
        """
        if days_back <= 1:
            return "qdr:d"
        elif days_back <= 7:
            return "qdr:w"
        elif days_back <= 30:
            return "qdr:m"
        else:
            return "qdr:y"


class MultiATSQueryBuilder:
    """
    Generates queries across all configured ATS platforms for a given search.
    This is the entry point you'll call from the scraper.
    """

    def __init__(self, platforms: list[ATSConfig] = ATS_PLATFORMS):
        self.platforms = platforms

    def build_all(self, params: SearchParams) -> list[tuple[ATSConfig, str, str]]:
        """
        Returns a list of (ats_config, query_string, first_page_url) tuples.
        One tuple per ATS platform — the scraper iterates over these.
        """
        results = []
        for ats in self.platforms:
            builder = QueryBuilder(ats)
            query_str = builder.build_query_string(params)
            first_url = builder.build_url(params, page=0)
            results.append((ats, query_str, first_url))
        return results

    def build_paginated(
        self, params: SearchParams, ats: ATSConfig, max_pages: int
    ) -> list[tuple[int, str]]:
        """
        Returns all paginated URLs for a single ATS platform.
        Use this once you've confirmed results exist on page 1.
        """
        builder = QueryBuilder(ats)
        return [(page, builder.build_url(params, page=page)) for page in range(max_pages)]
