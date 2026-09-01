# analyticsdev.net — Website

Static conference website for [AnalyticsDev](https://analyticsdev.net), a code-first evening event for technical digital analysts and data engineers.

Hosted on **GitHub Pages**. Edit HTML files directly and push to `main` — no build step needed.

> **New to this?** Start with **[onboarding.md](onboarding.md)** — a from-scratch guide
> covering GitHub accounts, VS Code, and how to make your first change safely. This
> README assumes you already have access and know the workflow.

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

### 6. Add a webcast episode

Episodes live on their own page, `webcast/index.html`, **not** on the event page. The series continues between conferences, so the page is deliberately not tied to a year — that way the back catalogue does not get archived along with each edition.

Open `webcast/index.html` and find the `<section id="episodes">` block.

1. **Copy the whole `<article class="episode">` block**, from the `<!-- EPISODE -->` comment down to `</article>`.
2. **Paste it above the existing one.** Newest episode goes first.
3. Update the fields marked `<!-- EDIT: ... -->`:
   - **Episode number and date** — `Episode 02 · 14 October 2026`
   - **Title** and **guests** (guest first, then the hosts)
   - **Video** — see below
   - **Description** — one or two paragraphs
   - **Takeaway** — the one-line summary. Delete the whole `<p class="episode-takeaway">` block if the episode does not have one.
   - **Spotify link** — see below

**The video.** On the video's page, use **Share → Embed** and copy the code. It looks like this:

```html
<div style="width:100%; height:0; position: relative; padding-bottom:56.25%"><iframe title="Video Player" src="//blc.twentythree.com/..." style="..." frameborder="0" ...></iframe></div>
```

You only need the `src` — paste it into the `src="..."` of the iframe already in the block, and leave everything else alone. The sizing is handled by `css/style.css`, so the `style="..."` attributes in the copied code are not needed.

> **Two things to check.** If the URL ends in `&autoPlay=1`, **delete that part** — otherwise the video starts playing by itself the moment someone opens the page. And if the URL starts with `//`, change it to `https://`.

**The Spotify link.** Episodes go up on Spotify after the live broadcast, so a new episode starts with this placeholder line:

```html
<p class="episode-links episode-links-pending">Audio version coming to Spotify</p>
```

Once the episode is live on Spotify, replace that whole line with:

```html
<p class="episode-links"><a href="PASTE_SPOTIFY_URL" target="_blank" rel="noopener">Listen on Spotify &rarr;</a></p>
```

**Do not** change the navigation on `webcast/index.html` — it deliberately matches the home page nav, with `/#about`-style links so the items still reach the home page's sections.

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
├── webcast/
│   └── index.html        # Webcast Series — episodes, not tied to any year
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

Until the zone is updated, **Settings → Pages** shows "DNS Check in Progress"
and greys out **Enforce HTTPS**. Both are expected while the apex still resolves
to the old forwarder, and clear on their own once the records propagate.

**4. Turn on HTTPS**

Once DNS resolves to the GitHub IPs, tick **Enforce HTTPS** in **Settings → Pages**. The certificate is issued automatically — usually within minutes, occasionally up to 24 hours.

---

### Three things to watch

**Underscore-prefixed files are not published.** GitHub Pages runs Jekyll by default, which skips files and folders starting with `_` — so `_test.html` and `2026/_test.html` stay out of the live site. To bypass Jekyll entirely, add an empty `.nojekyll` file at the repo root, but rename the test files first or they will go live.

**The internal docs are excluded from the live site.** `_config.yml` lists `README.md`, `SPEC.md`, `TODO.md` and `onboarding.md` under `exclude`, so they stay in the repository but are never copied to `analyticsdev.net`. This depends on Jekyll running — adding a `.nojekyll` file switches Jekyll off and would publish all four at URLs like `analyticsdev.net/onboarding.md`. Note that "excluded from the site" is not the same as private: the repo itself is public, so anyone can still read them on GitHub.

**Absolute links only work on the custom domain.** The archive links use absolute paths like `href="/2026/"`. Those resolve correctly at `analyticsdev.net`, but break if the site is previewed at a repo subpath (e.g. `gunnargriese.com/analyticsdev/`) before DNS is live. Expect broken archive links during that window only.
