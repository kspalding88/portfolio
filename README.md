# Kyle Spalding — Data Science Portfolio

**Live site:** https://kspalding88.github.io/portfolio/

This repository holds the presentation layer of my data science portfolio: a
single-page, vertical-scroll website built with plain HTML, CSS, and a few lines
of JavaScript, deployed with **GitHub Pages**. It is built for a reviewer who
has only a couple of minutes — the hero and projects communicate the essentials
up front.

## What's here

| File | Purpose |
|------|---------|
| `index.html` | The full portfolio page (Hero, About, Projects, Contact) |
| `assets/style.css` | All styling — dark theme, responsive layout |
| `assets/main.js` | Mobile nav toggle and footer year |
| `.nojekyll` | Tells GitHub Pages to serve the `assets/` folder as-is |

## Sections

- **About** — I lead as a data scientist completing a Master of Data Science,
  with 6+ years in network operations presented as supporting context, plus an
  at-a-glance card and toolbox.
- **Projects** — the fully populated section. Three curated data science
  projects, each with problem, method, a concrete result, tools, and a repo
  link.
- **Contact** — email, GitHub, and LinkedIn.

A hero/cover section sits above these to deliver the quick "couple of minutes of
attention" hook.

## Projects shown

1. **Beer Strength (ABV) Prediction** — supervised regression. Lasso vs. Random
   Forest in scikit-learn pipelines; Random Forest reached 0.84 percentage
   points of ABV mean absolute error vs. 1.40 points for Lasso.
2. **Mushroom Edibility Classification** — supervised classification optimized
   for recall on the poisonous class, with safety-first threshold tuning.
3. **Network Ticket Summarization Tool** — text parsing and standardization that
   turns unstructured trouble-ticket text into structured, analyzable records.

The scope is deliberately data-science-first: regression, classification, and
text-to-structured-data work. My network operations background appears as
supporting context rather than the headline.

## Design intent

- **One page, vertical scroll** so a reviewer can skim the whole portfolio
  without clicking.
- **Data science leads**, with network operations framed as a differentiator —
  real experience with high-volume, noisy, time-sensitive data.
- **Honest results.** Every project card states a concrete outcome and the skill
  it demonstrates, not just a title.

## Deploy / update

This site deploys from the `main` branch root via **Settings → Pages → Deploy
from a branch → `main` / `/ (root)`**. After any change, push to `main` and
GitHub Pages rebuilds automatically within a minute or two.

## Preview locally

From the repository root:

```bash
python -m http.server 8000
```

Then open <http://localhost:8000> in a browser.
