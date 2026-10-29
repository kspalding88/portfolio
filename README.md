# Portfolio Milestone 2 — Public-Facing Portfolio

**Kyle Spalding**

This folder contains the presentation layer of my data science portfolio: a
single-page, vertical-scroll website built with plain HTML, CSS, and a few lines
of JavaScript. It is designed to deploy as a **GitHub Pages** site and to grab a
reviewer's attention in the first few seconds.

## What's here

| File | Purpose |
|------|---------|
| `index.html` | The full portfolio page (Hero, About, Projects, Contact) |
| `assets/style.css` | All styling — dark theme, responsive layout |
| `assets/main.js` | Mobile nav toggle and footer year |
| `.nojekyll` | Tells GitHub Pages to serve the `assets/` folder as-is |

## Required sections (assignment)

- **About** — background, the NOC-to-data-science story, and an at-a-glance card.
- **Projects** — the section I chose to **fully populate** for this milestone.
  Six project cards drawn from real work, each with problem, method, result,
  tools, and a repo link.
- **Contact** — email, GitHub, and a LinkedIn placeholder.

A hero/cover section sits above these to deliver the "couple of minutes of
attention" hook the assignment describes.

## Design intent

- **One page, vertical scroll** for low friction — a reviewer can skim the whole
  portfolio without clicking.
- **Projects first in emphasis.** The hook leads with the operations-to-analytics
  angle so the portfolio appeals to Data Analyst / NOC-adjacent roles.
- **Honest results.** Every project card states a concrete outcome and the skill
  it demonstrates, not just a title.

## Milestone 1 feedback addressed

- **Beer metric units fixed.** The card now reads *0.84 percentage points of ABV*
  vs *1.40 points* and explicitly notes this is ABV error, **not** a percentage
  of error.
- **No Bellevue / course numbers.** The site refers to "a Master of Data Science"
  and describes projects by subject/method only.
- **Range of skills shown.** Beyond the two original ML projects, the Projects
  section now includes data visualization (Vehicle Theft story in R), analytics
  (TSA complaints), automation (ticket summarization), and a data pipeline — so
  the portfolio shows visualization, time-series/seasonality, and data wrangling.
- **Cleanup described.** A note under Projects explains what was consolidated,
  renamed, and archived.
- **README included for review.** This file is the submission write-up.

## Deploy to GitHub Pages

Two common options:

### Option A — dedicated portfolio repo (recommended)
1. Create a repo, e.g. `kspalding88/portfolio` (or `kspalding88.github.io` for a
   root-level site).
2. Copy the contents of this folder (`index.html`, `assets/`, `.nojekyll`) into
   the repo root.
3. Push to GitHub.
4. In the repo: **Settings → Pages → Build and deployment → Source: Deploy from a
   branch**, pick `main` and `/ (root)`, save.
5. The site publishes at `https://kspalding88.github.io/portfolio/`
   (or `https://kspalding88.github.io/` for the user-site repo).

### Option B — serve this subfolder from an existing repo
1. Move `index.html`, `assets/`, and `.nojekyll` to the repo root (Pages serves
   from root or `/docs`, not an arbitrary subfolder).
2. Enable Pages as above.

## Preview locally

From this folder:

```bash
python -m http.server 8000
```

Then open <http://localhost:8000> in a browser.

## To do before final submission

- Replace the LinkedIn placeholder in the Contact section with your real URL.
- Publish the remaining project repos and swap the "publishing" links for live
  repository URLs.
