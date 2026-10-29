# Kyle Spalding — Data Science Portfolio

**Live site:** https://kspalding88.github.io/portfolio/

This repository holds the source for my data science portfolio: a single-page,
vertical-scroll site built with the **[Pelican](https://getpelican.com/)**
static site generator (Python) and deployed with **GitHub Pages**. It is built
for a reviewer who has only a couple of minutes — the hero and projects
communicate the essentials up front.

## How it's built

Pelican is a Python static site generator. The site source lives on the `main`
branch; the generated HTML is published to the `gh-pages` branch, which GitHub
Pages serves.

```
content/          Page content (Markdown)
  pages/home.md     The landing page (uses the custom "portfolio" template)
  extra/.nojekyll   Passed through so Pages skips a second Jekyll build
theme/            Custom Pelican theme (reproduces the portfolio design)
  templates/        base.html + portfolio.html (hero, about, projects, contact)
  static/css        style.css
  static/js         main.js
pelicanconf.py    Development config
publishconf.py    Production config (sets the public SITEURL)
requirements.txt  Python dependencies
```

## Sections

- **About** — I lead as a data scientist completing a Master of Data Science,
  with 6+ years in network operations presented as supporting context, plus an
  at-a-glance card and toolbox.
- **Projects** — the fully populated section. Three curated data science
  projects, each with problem, method, a concrete result, tools, and a repo
  link.
- **Contact** — email, GitHub, and LinkedIn.

## Projects shown

1. **Beer Strength (ABV) Prediction** — supervised regression. Lasso vs. Random
   Forest in scikit-learn pipelines; Random Forest reached 0.84 percentage
   points of ABV mean absolute error vs. 1.40 points for Lasso.
2. **Mushroom Edibility Classification** — supervised classification optimized
   for recall on the poisonous class, with safety-first threshold tuning.
3. **Network Ticket Summarization Tool** — text parsing and standardization that
   turns unstructured trouble-ticket text into structured, analyzable records.

## Build and preview locally

```bash
# 1. (Optional) create and activate a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Build the site
python -m pelican content -s pelicanconf.py

# 4. Preview
cd output
python -m http.server 8000
# open http://localhost:8000
```

## Deploy to GitHub Pages

The site is published to the `gh-pages` branch with `ghp-import`:

```bash
# Build with the production config (absolute URLs)
python -m pelican content -s publishconf.py

# Publish the output/ folder to the gh-pages branch and push
ghp-import output -b gh-pages -m "Publish site"
git push origin gh-pages
```

GitHub Pages is configured under **Settings → Pages → Deploy from a branch →
`gh-pages` / `/ (root)`**. The site rebuilds a minute or two after the push.
