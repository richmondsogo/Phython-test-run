from models import ATSConfig

# Each entry maps to a Google site: operator.
# These are the ATS platforms job boards funnel back to anyway —
# we're just skipping the middleman.
ATS_PLATFORMS: list[ATSConfig] = [
    ATSConfig(name="greenhouse", site_operator="greenhouse.io", label="Greenhouse"),
    # ATSConfig(name="lever", site_operator="jobs.lever.co", label="Lever"),
    # ATSConfig(name="ashby", site_operator="jobs.ashbyhq.com", label="Ashby"),
    # ATSConfig(name="workable", site_operator="apply.workable.com", label="Workable"),
    # ATSConfig(name="bamboohr", site_operator="bamboohr.com/careers", label="BambooHR"),
    # ATSConfig(name="jobvite", site_operator="jobs.jobvite.com", label="Jobvite"),
    # ATSConfig(name="notion", site_operator="notion.site", label="Notion"),
    # ATSConfig(
    #     name="smartrecruiters",
    #     site_operator="jobs.smartrecruiters.com",
    #     label="SmartRecruiters",
    # ),
    # ATSConfig(name="icims", site_operator="icims.com", label="iCIMS"),
    # ATSConfig(name="personio", site_operator="jobs.personio.com", label="Personio"),
    # ATSConfig(name="teamtailor", site_operator="teamtailor.com", label="Teamtailor"),
    # ATSConfig(name="recruitee", site_operator="recruitee.com", label="Recruitee"),
    # ATSConfig(name="breezy", site_operator="breezy.hr", label="Breezy HR"),
    # ATSConfig(name="workday", site_operator="myworkdayjobs.com", label="Workday"),
    # ATSConfig(name="taleo", site_operator="taleo.net/careersection", label="Taleo"),
    # ATSConfig(name="jobadder", site_operator="jobadder.com", label="JobAdder"),
    # ATSConfig(name="jazzhr", site_operator="applytojob.com", label="JazzHR"),
    # ATSConfig(name="avature", site_operator="avature.net", label="Avature"),
    # ATSConfig(
    #     name="successfactors", site_operator="jobs.sap.com", label="SAP SuccessFactors"
    # ),
]

# Google SERP settings
GOOGLE_BASE_URL = "https://www.google.com/search"
RESULTS_PER_PAGE = 10
MAX_PAGES = 3  # 30 results per ATS query — tune this up once pipeline is stable

# Playwright timeouts (ms)
PAGE_LOAD_TIMEOUT = 15_000
ELEMENT_TIMEOUT = 8_000

# Human-like delay range between actions (seconds)
DELAY_MIN = 1.2
DELAY_MAX = 3.5
