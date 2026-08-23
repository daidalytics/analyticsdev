# analyticsdev.net — Website

Static conference website for [AnalyticsDev](https://analyticsdev.net), a code-first evening event for technical digital analysts and data engineers.

Hosted on **GitHub Pages**. Edit HTML files directly and push to `main` — no build step needed.

---

## How to update the site

All editable areas are marked with `<!-- EDIT: ... -->` comments inside the HTML files. Open the file in any text editor, find the comment, and update the content below it.

### 1. Update the event date, venue, and registration link

Open `index.html` and find:

```html
<!-- EDIT: Update date and venue below -->
<div class="hero-meta">
  29 April 2026 ...
</div>

<!-- EDIT: Update the Billetto href below when a new event opens for registration -->
<a href="https://billetto.dk/..." ...>Register on Billetto</a>
```

Also update the `<title>` and `<meta name="description">` at the top of `index.html`.

---

### 2. Update the programme / schedule

Open `index.html` and find the `<!-- EDIT: Add, remove, or edit time slots below -->` comment inside the `<section id="programme">` block.

Each time slot looks like this:

```html
<li class="programme-item">
  <span class="programme-time">15:00</span>
  <div class="programme-desc">Arrival &amp; Registration</div>
</li>
```

Copy, paste, and edit as needed.

---

### 3. Update speaker cards

Open `index.html` and find the `<section id="speakers">` block.

Each speaker card looks like this:

```html
<div class="speaker-card">
  <img class="speaker-photo" src="assets/speakers/firstname-lastname.jpg" alt="Full Name">
  <div class="speaker-info">
    <p class="speaker-name">Full Name</p>
    <p class="speaker-role text-muted">Title · Company</p>
    <details class="speaker-details">
      <summary>Bio &amp; Session</summary>
      <p class="speaker-bio">Short bio here.</p>
      <p class="speaker-session-label">Session</p>
      <p class="speaker-session">Session title and description here.</p>
    </details>
  </div>
</div>
```

To add a speaker: copy the block above and paste it inside the `<div class="speakers-grid">`.
To remove a speaker: delete the entire `<div class="speaker-card">...</div>` block.

**Adding a speaker photo:**
1. Add the photo file to `assets/speakers/` (square crop recommended, e.g. `mark-edmondson.jpg`)
2. Replace the `<div class="speaker-photo-placeholder">` with:
   ```html
   <img class="speaker-photo" src="assets/speakers/mark-edmondson.jpg" alt="Mark Edmondson">
   ```

---

### 4. Update sponsors / partners

Open `index.html` and find `<section id="partners">`.

**To replace a sponsor logo:**
1. Add the logo file to `assets/sponsors/` (SVG or PNG, transparent background)
2. Replace the `<span class="sponsor-logo-placeholder">Name</span>` with:
   ```html
   <img src="assets/sponsors/stape.png" alt="Stape.io" style="height:60px;">
   ```

**To change the Gold Partner:** update the name, `href`, and logo inside `.sponsor-tier--gold`.
**To add/remove a Supporting Partner:** copy or delete an `<a class="sponsor-logo-link">` block inside `.sponsor-tier--supporting`.

---

### 5. Archive an event (after the event has passed)

1. **Copy** `index.html` to `2026/index.html` (replace `2026` with the actual year)
2. In the copied file:
   - Change the `<link rel="stylesheet" href="css/style.css">` to `../css/style.css`
   - Change logo and asset paths from `assets/...` to `../assets/...`
   - Remove the register button and replace with the "event passed" message
   - Add the archive banner at the top (see `2026/index.html` for reference)
3. In the root `index.html`, add the past edition to the archive list:
   ```html
   <li>
     <a href="/2026/">2026 · 29 April — Campus Carlsberg, Copenhagen</a>
   </li>
   ```
4. Remove the placeholder text: `<p class="archive-empty">Archive coming after the first edition...</p>`
5. Update the root `index.html` with the new event's details (date, venue, Billetto URL)
6. Push to GitHub

> The `2026/index.html` file in this repo is already set up as a template — use it as a reference.

---

## File structure

```
analyticsdev.net/
├── index.html            # Current/upcoming event (edit this for each new edition)
├── CNAME                 # GitHub Pages domain — do not edit
├── favicon.ico           # Generated — see "Favicon" below
├── README.md             # This file
├── css/
│   └── style.css         # All styles — colours and fonts can be updated here
├── assets/
│   ├── favicon.svg       # The favicon mark — source of truth for the shape
│   ├── apple-touch-icon.png  # Generated — see "Favicon" below
│   ├── logo/
│   │   └── image.png     # Current logo (replace with AnalyticsDev logo when ready)
│   ├── speakers/         # Speaker headshots — add files here
│   └── sponsors/         # Sponsor logos — add files here
├── tools/
│   └── render-favicon.py # Regenerates favicon.ico and apple-touch-icon.png
└── 2026/
    └── index.html        # Archive: 2026 edition
```

---

## Favicon

The mark is two monospace slashes carrying the wordmark's weight break: a
hairline "Analytics" slash and a bold "Dev" slash on the site's ink.

`assets/favicon.svg` is the source of truth. `favicon.ico` and
`assets/apple-touch-icon.png` are rasterised from the same geometry, which is
duplicated in `tools/render-favicon.py`. To change the mark, edit both the SVG
and the geometry constants in the script, then run:

```bash
python3 tools/render-favicon.py
```

No packages to install — the script writes PNG and ICO by hand.

---

## Colours and fonts

All colours are defined as CSS variables at the top of `css/style.css`:

```css
:root {
  --color-accent-hl: #22c55e;  /* Green used on buttons and highlights */
  /* ... */
}
```

Change `--color-accent-hl` to update the primary accent colour across the whole site.

---

## Local development

To preview the site locally, start a simple HTTP server from the project root:

```bash
python3 -m http.server 8000
```

Then open [http://localhost:8000](http://localhost:8000) in your browser.

---

## Deploying

### Day-to-day

1. Push changes to the `main` branch on GitHub
2. GitHub Pages automatically serves the updated site at `analyticsdev.net`
3. The `CNAME` file tells GitHub Pages which domain to use — do not delete it

If the site does not update, go to **Settings → Pages** in the GitHub repo and confirm Pages is enabled for the `main` branch.

---

### First-time setup (one-off)

This site is a GitHub Pages **project site** owned by the `daidalytics` account — one repo, one custom domain. It is entirely independent of the `gunnargriese.github.io` user site that serves `gunnargriese.com`: an account may have only one user site, but any number of project sites, each with its own domain.

**1. Create the repo and push**

```bash
cd analyticsdev
git init -b main
git add .
git commit -m "Initial commit: analyticsdev.net site"
gh auth login
gh repo create daidalytics/analyticsdev --public --source=. --push
```

> If a push fails with `RPC failed; HTTP 400`, the pack has exceeded git's 1 MB default `http.postBuffer` and switched to chunked encoding. Fix with `git config http.postBuffer 524288000`, or fall back to `git config --global http.version HTTP/1.1`, or use the SSH remote `git@github.com:daidalytics/analyticsdev.git`.

**2. Enable GitHub Pages**

In the repo: **Settings → Pages → Source: Deploy from a branch → `main` / `(root)`**.
GitHub reads the existing `CNAME` file and fills in the custom domain automatically.

**3. Point DNS at GitHub**

`analyticsdev.net` is registered with **Simply.com** (nameservers `ns1–ns3.simply.com`), so edit the zone there. Replace the existing apex `A` record with:

| Type  | Host  | Value                    |
| ----- | ----- | ------------------------ |
| A     | `@`   | `185.199.108.153`        |
| A     | `@`   | `185.199.109.153`        |
| A     | `@`   | `185.199.110.153`        |
| A     | `@`   | `185.199.111.153`        |
| AAAA  | `@`   | `2606:50c0:8000::153`    |
| AAAA  | `@`   | `2606:50c0:8001::153`    |
| AAAA  | `@`   | `2606:50c0:8002::153`    |
| AAAA  | `@`   | `2606:50c0:8003::153`    |
| CNAME | `www` | `daidalytics.github.io.`  |

The `www` CNAME must point at the **owner of this repo** (`daidalytics`), not at a personal account. The four A records are the shared GitHub Pages IPs and are the same ones used by the `gunnargriese.com` apex, so those can be copied from that domain's zone. Confirm against the [GitHub Pages docs](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site) before pasting, in case the addresses have changed.

Check propagation with:

```bash
dig +short analyticsdev.net A
dig +short www.analyticsdev.net
```

<details>
<summary><strong>Brief for the domain administrator</strong> (copy-paste)</summary>

If someone else administers the zone, send them this. It is deliberately plain
text — most chat clients render markdown syntax literally.

```
Hi Jens,

The AnalyticsDev page is built and live on GitHub Pages — repo is
daidalytics/analyticsdev (public). Ready for the DNS cutover whenever suits you.

Two things needed on analyticsdev.net (nameservers are Simply.com):

1. Remove the existing URL forwarding.
The apex currently points to 94.231.103.100, Simply's URL-forwarder, which 302s
to brandleadership.community/Insights/analytics-dev-17-march-2027/. Please
disable the forwarding in Simply's control panel rather than only deleting the
A record, so it doesn't get re-added automatically.

2. Add these records.

Apex (analyticsdev.net) — four A records:
  185.199.108.153
  185.199.109.153
  185.199.110.153
  185.199.111.153

Apex (analyticsdev.net) — four AAAA records, optional but recommended:
  2606:50c0:8000::153
  2606:50c0:8001::153
  2606:50c0:8002::153
  2606:50c0:8003::153

www — one CNAME:
  www.analyticsdev.net.  CNAME  daidalytics.github.io.

GitHub then redirects www to the apex automatically. Four A records rather than
a single alias because DNS doesn't permit a CNAME at the zone apex — they're
GitHub's anycast edge servers, and the site is selected by the Host header.

There are no MX or TXT records on the domain today, so nothing else is affected
and there's no email to disrupt. Current TTL is around 10 minutes, so the
cutover should propagate quickly.

Once it resolves, GitHub issues a Let's Encrypt certificate automatically,
usually within the hour, and I'll enable "Enforce HTTPS" from our side. That
also clears the browser security warnings you saw on the old redirect, since
the domain gets a real certificate of its own for the first time.

The new page links out to BLC and Billetto, so the destinations the old
redirect covered stay reachable.

Happy to jump on a quick call if easier. Thanks!

Gunnar
```

Until the zone is updated, **Settings → Pages** shows "DNS Check in Progress"
and greys out **Enforce HTTPS**. Both are expected while the apex still resolves
to the old forwarder, and clear on their own once the records propagate.

</details>

**4. Turn on HTTPS**

Once DNS resolves to the GitHub IPs, tick **Enforce HTTPS** in **Settings → Pages**. The certificate is issued automatically — usually within minutes, occasionally up to 24 hours.

---

### Two things to watch

**Underscore-prefixed files are not published.** GitHub Pages runs Jekyll by default, which skips files and folders starting with `_` — so `_test.html` and `2026/_test.html` stay out of the live site. To bypass Jekyll entirely, add an empty `.nojekyll` file at the repo root, but rename the test files first or they will go live.

**Absolute links only work on the custom domain.** The archive links use absolute paths like `href="/2026/"`. Those resolve correctly at `analyticsdev.net`, but break if the site is previewed at a repo subpath (e.g. `gunnargriese.com/analyticsdev/`) before DNS is live. Expect broken archive links during that window only.
