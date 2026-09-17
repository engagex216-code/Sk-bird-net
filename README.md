# SK Bird Net Solutions — Website

Static 4-page marketing site for SK Bird Net (bird netting, child safety net,
sport net, balcony netting, residential bird net, invisible grill, bamboo chick).

## Pages
- `index.html` — Home (hero, services grid, stats, testimonials, gallery, customer feedback)
- `services.html` — Detailed breakdown of all 7 services
- `about.html` — Company story, values, stats
- `contact.html` — Quote form, address, phone, hours

## Structure
- `assets/` — all photos and videos used across the site. Keep this folder
  alongside the HTML files — the pages reference it with relative paths
  (e.g. `assets/hero-balcony.jpg`). Do not rename files inside without
  updating the matching `<img>`/`<video>` tag.
- `favicon.svg`, `site.webmanifest` — site icon and PWA metadata
- `robots.txt`, `sitemap.xml` — basic SEO files
- `build.py` — the Python script that generates all 4 HTML files from
  shared header/footer/stats templates. Edit this and rerun it rather than
  hand-editing the HTML files directly, so all pages stay in sync.

## Contact number
WhatsApp / phone: +91 88780 20513 (update in `build.py` if it changes —
appears in the floating WhatsApp button, header, and footer on every page).

## Hosting
Deployed via GitHub Pages from the `main` branch, root folder.
Live at: https://engagex216-code.github.io/Sk-bird-net/
