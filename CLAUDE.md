# CFB-mapping

Last updated: 2026-03-22 (Phase 4 P4 — DEC-GLOBAL-030)

**Repo**: `https://github.com/verifygrit-admin/CFB-mapping` (public)
**Path**: `C:\Users\chris\dev\CFB-mapping`

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
| `type` | School selectivity tier (see thresholds below) |
| `adltv` | Adjusted Lifetime Value |
| `adltv_rank` | ADLTV rank |
| `adm_rate` | Admissions rate |
| `grad_rate` | Graduation rate |
| `coa_out` | Cost of attendance (out-of-state) |
| `merit` | Merit aid estimate |
| `q_link` | Recruiting questionnaire URL — 592 of 661 populated |
| `coach_link` | Football coaching staff page URL — 552 of 661 populated |

## School Selectivity Tiers (`type` field)

| Value | Admissions Rate | Schools |
|---|---|---|
| `Super Elite` | ≤ 10% | 22 |
| `Elite` | 11–19% | 27 |
| `Very Selective` | 20–29% | 18 |
| `Selective` | 30–49% | 54 |
| `Somewhat Selective` | 50–67% | 95 |
| `Standard` | > 67% | 445 |

Used by the **Admissions Selectivity** sidebar filter (label updated from "School Type (Selectivity)"). Thresholds are applied to the `adm_rate` field at data-build time; the filter matches `s.type` directly at runtime. The school popup displays this value under the label **"Admissions Select."**

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
- Primary accent (CSS var): `#6ed430` (neon green — hover/brand use only); active filter buttons use `#2e6b18` (dark forest green) with `#c8f5a0` light text
- Tier colors: Power 4 `#f5a623`, FCS `#81c784`, FBS Ind `#ce93d8`, D2 `#ef9a9a`, D3 `#b0bec5`, G5 `#4fc3f7`
- Fonts: Barlow Condensed (headers/logo), Barlow (body)

### Marker Cluster Colors
- Small cluster: `rgba(46,107,24)` background, `#c8f5a0` text
- Medium cluster: `rgba(36,84,18)` background, `#c8f5a0` text
- Large cluster: `rgba(26,60,13)` background, `#c8f5a0` text

## Helmet Animation

On page load, `helmet.png` (RGBA PNG, 1080x1350, in project root) plays a two-phase animation:

**Phase 1** — CSS `@keyframes helmetReveal` over 2.8s: image appears at viewport center, grows and bounces twice.

**Phase 2** — JS transition over 0.5s: image translates to `#tutHelpBtn` using `translate(dx,dy) scale(0.12)`, flying from center to the help button.

First-time tutorial auto-open fires 4.5s after page load. All animation JS lives in the final `<script>` block.

## Mobile Constraints

- `#tutHelpBtn` tap target: 44px minimum
- iOS zoom fix: `font-size: 16px` on all input/select at `≤768px`
- Header padding tightened at mobile breakpoints
- `-webkit-tap-highlight-color` suppressed globally
- School count hidden at `≤360px` viewport width

## Data Stewardship

**David (Data Steward)** owns master DB integrity and link rot monitoring. Trigger: `david -`.

Source of truth for q_link and coach_link: Google Sheet (ID: `1Pc4LOnD1fhQz-9pI_CUEDaAMDfTkUXcCRTVDfoDWvqo`, tab: GrittyOS DB). CSV in recruitingq-url-extract is a pipeline artifact — downstream of Sheet.

**PROTO-GLOBAL-010**: Any output used as a build pre-condition must name the source artifact explicitly.

## Deployment
Static file — open directly in browser or serve from any static host. Push to GitHub; no CI/CD configured.
