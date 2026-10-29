"""Production Pelican config for GitHub Pages.

Used for the published build: `pelican content -s publishconf.py`.
Inherits everything from pelicanconf.py and sets the public site URL.
"""

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa: F401,F403

# The project lives at https://kspalding88.github.io/portfolio/
SITEURL = "https://kspalding88.github.io/portfolio"
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True
