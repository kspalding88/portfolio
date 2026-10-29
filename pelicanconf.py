AUTHOR = 'Kyle Spalding'
SITENAME = 'Kyle Spalding — Data Science Portfolio'
SITEDESCRIPTION = (
    'Portfolio of machine learning, analytics, and data visualization projects '
    'by Kyle Spalding.'
)
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# --- Portfolio customizations -----------------------------------------------
# This site is a single landing page rather than a blog, so the quickstart
# defaults above are adjusted below.

# Use the custom theme that holds the portfolio design.
THEME = "theme"

# Render the "home" page as index.html so it becomes the site root.
PAGE_URL = "{slug}.html"
PAGE_SAVE_AS = "{slug}.html"

# Turn off the blog machinery: no articles, no blog index, and none of the
# category/tag/author/archive stub pages.
ARTICLE_PATHS = []
ARTICLE_SAVE_AS = ""
INDEX_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
TAGS_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""

# Pass .nojekyll through to the build so GitHub Pages skips its Jekyll step.
STATIC_PATHS = ["extra/.nojekyll"]
EXTRA_PATH_METADATA = {"extra/.nojekyll": {"path": ".nojekyll"}}
