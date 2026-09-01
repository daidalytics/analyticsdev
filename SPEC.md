# Spec: AnalyticsDev.net Webcast Series page

Status: **draft — awaiting approval**
Date: 2026-09-01

---

## Objective

Give the AnalyticsDev.net Webcast Series a permanent home on the site at
`analyticsdev.net/webcast/`, so episodes can accumulate across conference
editions instead of being buried when a year page is archived.

**Why a separate page and not a section on the 2027 event page.** The series is
defined as continuing the conversation *beyond* the conference. Episodes are
cross-year by nature — a March 2027 speaker interview is still worth watching in
2028. The site's existing lifecycle freezes each edition into `/YEAR/` and marks
it "This event took place on…"; a catalogue living inside that page would be
archived along with it and would need re-homing every single year. A standalone
page gives the series one stable URL to cite in Spotify show notes, LinkedIn
posts, and speaker outreach.

**Users**

| Who | What they came for |
|---|---|
| Technical analytics practitioners (analytics/data/AI engineers, martech, advanced digital analysts) | Watch or listen to an episode; find the rest of the catalogue |
| Prospective 2027 attendees arriving from a shared episode link | Understand what AnalyticsDev is and reach the event page |
| Prospective guests / future contributors | Understand the series' format and remit |
| Gunnar, or a non-developer editor | Add episode N+1 by copy-pasting one HTML block |

**Success looks like:** a new episode can be published by copying one commented
block, changing five fields, and pushing to `main` — no build step, no CSS
edits, no JavaScript changes.

### Acceptance criteria

1. `analyticsdev.net/webcast/` serves a page in the site's existing visual
   language — same nav, footer, typography, colour tokens, and container widths
   as [index.html](index.html).
2. The page carries, in order: series blurb, episode list (newest first), and a
   closing CTA to the AnalyticsDev 2027 event.
3. Episode 1 (Simo Ahava) is present with the TwentyThree video embed working.
4. Video does **not** autoplay on page load. The `autoPlay=1` parameter is
   stripped from the source URL.
5. Each episode block has a slot for a Spotify episode link that renders as a
   neutral "audio version coming soon" state while the URL is absent, and
   becomes a live link when one is pasted in — with no other markup change.
6. The page is linked from the main nav and the footer on the root page. **No
   teaser module on the home page** — the 2027 page stays focused on ticket
   conversion.
7. The page reads correctly at 1 episode and would still read correctly at 20.
8. Layout holds from 320px to 1440px wide; no horizontal page scroll.
9. `README.md` gains a numbered "Add a webcast episode" section matching the
   style of the existing update instructions.

### Naming

URL, nav label, and headings use **"Webcast Series"** (matching the official
framing). Body copy, meta description, and CTA wording also say **"podcast"**
and name **Spotify**, because that is how people search for it. Not a
contradiction — one is the product name, the other is the discovery term.

---

## Tech Stack

Unchanged from the rest of the site. This spec adds no dependencies.

- Static HTML5, hand-authored. **No build step.**
- One shared stylesheet, [css/style.css](css/style.css), using the existing
  `:root` colour tokens and IBM Plex Sans / IBM Plex Mono.
- Vanilla JS only, inline at the bottom of the page, same pattern as the mobile
  nav toggle and speaker carousel in [index.html](index.html).
- GitHub Pages + Jekyll. Jekyll is used **only** for the `exclude` list in
  [_config.yml](_config.yml) — no layouts, no collections, no data files.
- Third party: the BLC TwentyThree player (`blc.twentythree.com`), embedded as
  an `<iframe>`. Spotify: **link-out only, no embed.**

**No new tooling, no npm, no package.json, no Jekyll collections.** Adding any
of those would break the "anyone can edit the HTML" property the site is built
around.

---

## Commands

There is no build or test toolchain. These are the real commands.

```bash
# Local preview (from the project root)
python3 -m http.server 8000
# then open http://localhost:8000/webcast/

# Verify no stray autoplay parameter survived
grep -rn "autoPlay" webcast/index.html          # expect: no matches

# Verify internal links resolve to files that exist
grep -o 'href="/[^"]*"' webcast/index.html index.html | sort -u

# Publish
git add webcast/ index.html css/style.css README.md
git commit -m "Add Webcast Series page"
git push origin main                             # GitHub Pages deploys on push
```

**Local-preview caveat, already documented in README.md:** absolute links such
as `/webcast/` and `/2026/` resolve correctly on `analyticsdev.net` and under
`python3 -m http.server`, but break under VS Code Live Preview and under any
repo-subpath preview. Broken absolute links in those contexts are expected and
are not a bug.

---

## Project Structure

```
webcast/
  index.html        → NEW. The Webcast Series page. Self-contained, same
                      skeleton as 2026/index.html (nav, main, footer, inline
                      nav-toggle script).

assets/
  webcast/          → NEW. Episode thumbnails / guest photos for the series,
                      named firstname-lastname.jpg, matching the existing
                      assets/speakers/ convention.

css/style.css       → MODIFIED. New "WEBCAST" section appended near the archive
                      styles. Reuse .container, .btn, .section-intro,
                      .hero-eyebrow before writing anything new.

index.html          → MODIFIED. Nav link + footer link only. No new section.

README.md           → MODIFIED. New "6. Add a webcast episode" under
                      "How to update the site", plus webcast/ in File structure.

_config.yml         → UNCHANGED. Already excludes SPEC.md from the built site.
```

`2026/index.html` is **not touched.** It is a frozen archive.

---

## Code Style

Match the surrounding code exactly. The house style is heavily commented HTML
with `<!-- EDIT: ... -->` markers, because non-developers edit these files
directly.

### Episode block — the unit an editor copies

```html
<!-- ============================================================
     EPISODE — copy this whole block to add a new episode.
     Put the newest episode FIRST.
     ============================================================ -->
<article class="episode">

  <!-- EDIT: episode number, guest name, and broadcast date -->
  <p class="episode-meta">Episode 01 &middot; 12 September 2026</p>
  <h3 class="episode-title">Simo Ahava</h3>

  <!-- EDIT: one or two sentences on what the conversation covered -->
  <p class="episode-desc">
    …
  </p>

  <!-- EDIT: paste the TwentyThree share URL below.
       IMPORTANT: remove any "&autoPlay=1" from the end of the URL —
       video must never start on its own. -->
  <div class="episode-video">
    <iframe
      src="https://blc.twentythree.com/v.ihtml/player.html?source=site&amp;photo_id=130975359"
      title="AnalyticsDev Webcast — Simo Ahava"
      loading="lazy"
      allow="fullscreen"
      allowfullscreen
      referrerpolicy="no-referrer-when-downgrade"></iframe>
  </div>

  <!-- EDIT: when the Spotify episode is live, replace the <p> below with:
       <p class="episode-links"><a href="PASTE_SPOTIFY_URL" target="_blank"
          rel="noopener">Listen on Spotify &rarr;</a></p> -->
  <p class="episode-links episode-links-pending">Audio version coming to Spotify</p>

</article>
```

### CSS conventions

Tokens only — never a raw hex value. Comments explain *why*, in the voice of the
existing stylesheet.

```css
/* ============================================================
   WEBCAST SERIES
   ============================================================ */

/* 16:9 without a wrapper hack: the iframe fills a ratio-locked box. */
.episode-video {
  aspect-ratio: 16 / 9;
  border: 1px solid var(--color-border);
  background: var(--color-surface);
}

.episode-video iframe {
  width: 100%;
  height: 100%;
  border: 0;
  display: block;
}

/* The pending state is a statement of fact, not a dead link — muted, no
   underline, no pointer. It becomes a real link when the URL exists. */
.episode-links-pending {
  color: var(--color-text-muted);
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.85rem;
}
```

**Conventions**

- Two-space indent, double-quoted attributes, `&middot;` / `&mdash;` / `&rarr;`
  as HTML entities (matching existing files).
- Every external link: `target="_blank" rel="noopener"`.
- Every section: `aria-labelledby` pointing at its heading id.
- Lowercase monospace eyebrows in the site's path idiom —
  `analyticsdev.net / webcast`.
- Reuse before inventing: `.container`, `.btn`, `.btn-primary`,
  `.section-intro`, `.hero-eyebrow`, `.site-nav`, `.site-footer` already exist.

---

## Testing Strategy

There is no test framework and this spec does not add one — a four-file static
site does not earn a runner. Verification is a manual checklist, run against
`python3 -m http.server 8000` before every push.

| Level | What | How |
|---|---|---|
| Render | Page renders with correct nav, footer, fonts, colours | Open `localhost:8000/webcast/` |
| **Autoplay** | Video does **not** start on load | Load the page with sound on. Also `grep -rn "autoPlay" webcast/` → no matches |
| **Framing** | The TwentyThree iframe actually renders, not a blank box | Load page, check DevTools console for `X-Frame-Options` / CSP refusal |
| Responsive | 320px, 768px, 1440px — no horizontal scroll, video keeps 16:9 | DevTools device toolbar |
| Links | Nav, footer, `/webcast/`, `/2026/`, `/`, event CTA, Billetto | Click each one |
| Pending state | Spotify slot reads as "coming soon", is not a dead link | Visual |
| Scale | Duplicate the episode block 3× locally — layout still holds | Visual, then revert |
| A11y | Tab through the page; focus visible; headings nest h1→h2→h3 | Keyboard + DevTools accessibility tree |
| Deploy | Live at `analyticsdev.net/webcast/` after push | Browser, ~1 min after push |

**Risk to resolve in the first task, before anything else is built:** the
TwentyThree player may refuse to be framed by `analyticsdev.net`. Verify with a
throwaway local HTML file *before* building the page. If it is blocked, fall
back to a thumbnail card linking out to the BLC video page, and tell Gunnar —
do not silently ship an empty grey box.

---

## Boundaries

**Always**

- Preview locally with `python3 -m http.server 8000` before pushing.
- Strip `autoPlay=1` from every embed URL.
- Add `loading="lazy"` to every episode iframe.
- Use `:root` colour tokens; never a raw hex value in new CSS.
- Keep every editable region marked with an `<!-- EDIT: ... -->` comment.
- Reuse an existing CSS class before writing a new one.
- Update `README.md` in the same commit as the feature.

**Ask first**

- Anything that adds a build step, dependency, or Jekyll collection/data file.
- Embedding a second third-party iframe per episode (e.g. the Spotify player) —
  this spec deliberately links out instead.
- Changing the shared nav on `2026/index.html`, or any other archive edit.
- Adding analytics, consent banners, or cookie-setting scripts.
- Adding an RSS feed or self-hosting audio.
- Adding a teaser module to the 2027 home page — explicitly out of scope here.
- Changing site-wide tokens in `:root`.

**Never**

- Commit a `.nojekyll` file — it bypasses Jekyll and publishes `SPEC.md`,
  `README.md`, `TODO.md`, and `onboarding.md` to the live site.
- Delete or alter `CNAME`.
- Rewrite `2026/index.html` content — it is a historical record.
- Ship a dead or placeholder `href` (`href="#"` for a real destination).
- Ship an embed that autoplays with sound.
- Use uppercase or mismatched-case asset filenames — the live server is
  case-sensitive, macOS is not.

---

## Success Criteria

Done when all of the following are true:

1. `git push origin main` → `analyticsdev.net/webcast/` loads with the Simo
   Ahava episode, video playable on click, silent on load.
2. `grep -rn "autoPlay" webcast/` returns nothing.
3. Nav and footer on `analyticsdev.net` link to `/webcast/`; `/webcast/` links
   back to `/` and to the 2027 registration CTA. All click through.
4. The 2027 home page has **no** new content section — nav and footer links only.
5. No horizontal scroll at 320px; video holds 16:9 at every width.
6. Pasting a Spotify URL into the marked slot turns the pending line into a live
   link with no other edit required.
7. Duplicating the episode block yields a correct two-episode page.
8. `README.md` documents "Add a webcast episode" well enough for a
   non-developer to follow unaided.
9. `_config.yml` still excludes `SPEC.md`, and it is absent from the live site.

---

## Open Questions

1. **Episode 1 broadcast date and description.** Placeholder text is in the spec
   above; the real date and a 1–2 sentence summary of the Simo Ahava
   conversation are needed before publishing.
2. **Guest thumbnails.** `assets/speakers/2027/simo-ahava.jpg` already exists —
   reuse it, or use a per-episode still from the recording?
3. **TwentyThree framing.** Unverified. First task resolves it.
4. **Spotify show URL.** Launching later this month. Until then the page shows
   the pending state; a show-level link may be worth adding to the blurb once it
   exists, separately from the per-episode links.
5. **Backlink from BLC.** Should the BLC event page and Spotify show notes point
   at `/webcast/`? Outside this repo, but worth coordinating.
