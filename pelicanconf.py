"""Pelican configuration — Kyle Spalding Data Science Portfolio.

This site is a single custom-designed landing page, so the usual blog
machinery (articles, categories, tags, feeds, authors) is turned off and the
home page is rendered from a Pelican *page* with a dedicated template.
"""

AUTHOR = "Kyle Spalding"
SITENAME = "Kyle Spalding — Data Science Portfolio"
SITEDESCRIPTION = (
    "Portfolio of machine learning, analytics, and data visualization projects "
    "by Kyle Spalding."
)
SITEURL = ""

PATH = "content"
OUTPUT_PATH = "output"
TIMEZONE = "America/New_York"
DEFAULT_LANG = "en"

THEME = "theme"

# --- Single-page site: make the "home" page the landing page ----------------
PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"
# The "home" page becomes index.html (the site root).
PAGE_ORDER_BY = "slug"

# --- Turn off blog features we don't use ------------------------------------
ARTICLE_PATHS = []
ARTICLE_SAVE_AS = ""
ARTICLE_URL = ""
ARTICLE_LANG_SAVE_AS = ""
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""
PERIOD_ARCHIVES_SAVE_AS = ""
INDEX_SAVE_AS = ""  # no blog index; the page named "home" is the site index

# No Atom/RSS feeds for a portfolio landing page.
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# --- Static assets ----------------------------------------------------------
# The theme ships its own static files (CSS/JS); also copy .nojekyll through
# so GitHub Pages serves the built output without a second Jekyll pass.
STATIC_PATHS = ["extra/.nojekyll"]
EXTRA_PATH_METADATA = {"extra/.nojekyll": {"path": ".nojekyll"}}

DEFAULT_PAGINATION = False
RELATIVE_URLS = True

# Allow raw HTML blocks inside Markdown content.
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
    },
    "output_format": "html5",
}
