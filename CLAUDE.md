# CFB-mapping

## Purpose
Interactive map of all 661 NCAA college football programs for GritOS recruiting intelligence. Displays schools as clickable markers with recruiting data, filterable by division and tier.

## Stack
- Single self-contained HTML file (`cfbrecruit-map.html`) — no build step, no dependencies to install
- **Leaflet.js** (v1.9.4) — map rendering
- **Leaflet.markercluster** (v1.5.3) — marker clustering at zoom levels
- **D3.js** — data utilities
- **Google Fonts** — Barlow / Barlow Condensed
- All dependencies loaded via CDN (unpkg, Google)

## File Structure
```
CFB-mapping/
├── cfbrecruit-map.html      ← entire app (HTML + CSS + JS + data)
├── inject_coach_link.py     ← injects coach_link from GrittyOS DB CSV
├── CLAUDE.md
├── README.md
└── .gitignore               ← excludes *_backup_*.html and *.csv
```

## School Data
School data is embedded as a JSON array inside `cfbrecruit-map.html`. Each object has:

| Field | Description |
|---|---|
| `unitid` | IPEDS UNITID — primary key, used to join with GrittyOS DB CSV |
| `name` | School name |
| `div` | Division code: `1-FBS`, `1-FCS`, `2-Div II`, `3-Div III` |
| `tier` | Display tier: `Power 4`, `Group of 5`, `FCS`, `FBS Ind`, `Division II`, `Division III` |
| `conf` | Conference abbreviation |
| `city` / `state` | Location |
| `lat` / `lng` | Coordinates for map placement |
| `type` | School type |
| `adltv` | Adjusted Lifetime Value |
| `adltv_rank` | ADLTV rank |
| `adm_rate` | Admissions rate |
| `grad_rate` | Graduation rate |
| `coa_out` | Cost of attendance (out-of-state) |
| `merit` | Merit aid estimate |
| `q_link` | Recruiting questionnaire URL — 592 of 661 populated |
| `coach_link` | Football coaching staff page URL — 552 of 661 populated |

## Updating School Data
The source of truth for both `q_link` and `coach_link` is:
`C:\Users\chris\dev\recruitingq-url-extract\Gritty OS - CFB Recruiting Center - Example 2027 - GrittyOS DB.csv`

Join key: `UNITID` (CSV) → `unitid` (HTML object).

### To re-inject coach_link after CSV updates:
```
cd C:\Users\chris\dev\CFB-mapping
python inject_coach_link.py
```
Script is idempotent — strips existing `coach_link` values before re-injecting.

### To re-inject q_link (see recruitingq-url-extract project):
Drop updated CSV into this folder and run the injection script from that project.

## Design System
- Dark theme — CSS custom properties in `:root`
- Primary accent: `#6ed430` (green)
- Tier colors: Power 4 `#f5a623`, FCS `#81c784`, FBS `#ce93d8`, D2 `#ef9a9a`, D3 `#b0bec5`, G5 `#4fc3f7`
- Fonts: Barlow Condensed (headers/logo), Barlow (body)

## Deployment
Static file — open directly in browser or serve from any static host. Push to GitHub; no CI/CD configured.
