from pydantic import BaseModel, HttpUrl
from datetime import datetime
from typing import Optional


class ATSConfig(BaseModel):
    name: str
    site_operator: str  # used in Google's site: operator
    label: str          # human-readable label for logs


class SearchParams(BaseModel):
    job_title: str
    remote: bool = True
    days_back: int = 7  # keep listings fresh — default 1 week


class RawSearchResult(BaseModel):
    url: str
    title: str
    snippet: Optional[str] = None
    ats_source: str          # which ATS platform this came from
    query_used: str          # log exactly what query produced this result
    scraped_at: datetime = datetime.utcnow()
