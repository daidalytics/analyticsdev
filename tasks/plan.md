# Implementation Plan: AnalyticsDev.net Webcast Series page

Implements [SPEC.md](../SPEC.md). Status: **awaiting review**. Date: 2026-09-01.

---

## Overview

Add a standalone `/webcast/` page to the static site, carrying the series blurb,
a newest-first episode list starting with the Simo Ahava conversation, and a
closing CTA to AnalyticsDev 2027. Link it from the root page's nav and footer
only — no home-page teaser. No build step, no dependencies, no Jekyll
collections.

Total scope: **1 new file, 3 modified files, 1 new asset directory.** This is a
small feature; the plan is detailed because the failure modes are silent ones
(a blocked iframe renders as a grey box, misplaced CSS applies only on phones).

---

## Architecture Decisions

- **`webcast/index.html` is modelled on `2026/index.html`, not `index.html`.**
  The archive page is the site's existing example of a self-contained secondary
  page: relative stylesheet path (`../css/style.css`), root-absolute favicon
  paths, its own nav `<ul>` id, and one small inline nav-toggle script. The root
  page carries the hero panel, speaker carousel, and programme machinery — none
  of which this page needs.

- **Nav `<ul>` gets id `nav-links-webcast`.** The inline toggle script targets
  the id directly. Reusing `nav-links` invites a copy-paste collision later.

- **New CSS goes in before line 1506 of `css/style.css`**, immediately after the
  `EVENT STATS` block. The file ends inside `@media (max-width: 480px)`;
  appending at the end would scope the new rules to phones only. Responsive
  tweaks go into the existing 768/640/480 blocks.

- **The episode is `<article>`, the list is a plain stack, not a grid.** At one
  episode a grid looks broken; at twenty a stack still reads correctly. The
  spec requires both to hold.

- **Spotify is a link-out with a pending state, not an embed.** The show has not
  launched. The pending line is real markup an editor swaps for an `<a>` — not a
  disabled link, and not a commented-out block that will rot.

- **GTM `GTM-5Z4PKJ8L` is copied verbatim from the existing pages.** Same
  container, same head position, no `<noscript>` fallback (neither existing page
  has one). This corrects SPEC.md, which listed analytics under *Ask first*
  before the `<head>` had been read.

---

## Dependency Graph

```
Task 1  Framing spike (RISK — resolve first, branches everything below)
   │
   ▼
Task 2  webcast/index.html skeleton — nav, blurb, footer, CTA
   │        (renders correctly on existing CSS alone)
   │
   ├──────────────► Task 5  Root page nav + footer links   [independent]
   │                            │
   ▼                            │
Task 3  Episode 1 block ────────┤
   │                            │
   ▼                            │
Task 4  WEBCAST CSS section     │
   │                            │
   └──────────────┬─────────────┘
                  ▼
            Task 6  README documentation
                  │
                  ▼
            Task 7  Verification pass + deploy
```

Tasks 2→3→4 are one vertical slice built in three verifiable steps: the page
works after each, first on borrowed CSS, then with content, then styled. Task 5
is independent of that chain and can be done at any point after Task 2 fixes the
URL.

---

## Task List

### Phase 1: Resolve the risk

#### Task 1: Confirm the TwentyThree player can be framed

**Description:** The entire page design assumes `blc.twentythree.com` permits
embedding from another origin. If it sends `X-Frame-Options: DENY` or a
restrictive `frame-ancestors` CSP, the iframe renders as a blank box with only a
console error — a silent failure that looks like a CSS bug. Resolve this before
building anything.

**Method:** Write a throwaway HTML file in the scratchpad containing nothing but
the iframe, open it in a browser, and watch the console.

**Acceptance criteria:**
- [ ] The player either visibly renders and plays on click, or a specific
      refusal is captured from the console
- [ ] The finding is recorded in SPEC.md, replacing open question 3

**Verification:**
- [ ] Video visible and playable in the test file
- [ ] DevTools console shows no `X-Frame-Options` / `frame-ancestors` refusal

**If blocked:** stop and report. Fall back to a thumbnail card linking out to
the BLC video page — Tasks 2–7 stay valid, only the `.episode-video` block
changes. Do not ship an empty grey box.

**Dependencies:** None
**Files:** scratchpad only (no repo files)
**Scope:** XS

---

### Checkpoint: Risk resolved
- [ ] Framing confirmed working, **or** fallback approved by Gunnar
- [ ] SPEC.md open question 3 closed

---

### Phase 2: The page

#### Task 2: Create `webcast/index.html` skeleton

**Description:** The complete page — head, nav, series blurb, an empty episode
list region, event CTA, footer, inline nav script — using **only CSS classes
that already exist**. This proves the page is coherent on the site's existing
visual language before a single new rule is written.

Head mirrors `2026/index.html`: GTM snippet, `<title>AnalyticsDev Webcast
Series · Interviews with the speakers</title>`, meta description naming both
"webcast" and "podcast", `../css/style.css`, the three favicon links.

Content: `.hero-eyebrow` reading `analyticsdev.net / webcast`, an `<h1>`, the
series blurb from the brief, an `<h2>Episodes</h2>` region, and a closing CTA
linking to `/` with `.btn .btn-primary`.

**Acceptance criteria:**
- [ ] `localhost:8000/webcast/` renders with correct nav, fonts, colours, footer
- [ ] No unstyled or default-browser-looking elements
- [ ] Nav uses `id="nav-links-webcast"`; mobile toggle opens and closes
- [ ] Every section has `aria-labelledby`; headings nest h1→h2

**Verification:**
- [ ] `python3 -m http.server 8000`, open `/webcast/`
- [ ] Toggle the mobile nav at 375px
- [ ] `grep -c "GTM-5Z4PKJ8L" webcast/index.html` → `1`

**Dependencies:** Task 1
**Files:** `webcast/index.html`
**Scope:** S

---

#### Task 3: Add the episode 1 block

**Description:** Add the Simo Ahava episode as a copy-pasteable `<article
class="episode">` with the `<!-- EDIT: ... -->` markers from SPEC.md: episode
number and date, guest name, description, the ratio-locked iframe, and the
pending Spotify line. This is the block an editor duplicates for episode 2, so
its comments matter as much as its markup.

The embed URL is the supplied one **with `&autoPlay=1` removed**, plus
`loading="lazy"`, a descriptive `title`, and `allowfullscreen`.

**Acceptance criteria:**
- [ ] Video is visible and plays on click
- [ ] Page is silent on load — nothing starts on its own
- [ ] Spotify slot reads as a muted "coming to Spotify" line, not a dead link
- [ ] Every editable field carries an `<!-- EDIT: -->` comment

**Verification:**
- [ ] `grep -n "autoPlay" webcast/index.html` → no matches
- [ ] Load with sound on; confirm nothing plays
- [ ] Click play; confirm video runs

**Blocked on:** real broadcast date and a 1–2 sentence episode description
(SPEC.md open question 1). Ship with a clearly-marked placeholder if unanswered.

**Dependencies:** Task 2
**Files:** `webcast/index.html`
**Scope:** S

---

#### Task 4: Add the `WEBCAST SERIES` CSS section

**Description:** New styles for `.episode`, `.episode-meta`, `.episode-title`,
`.episode-desc`, `.episode-video`, `.episode-links`, `.episode-links-pending`,
and the episode stack.

**Inserted before line 1506**, after `EVENT STATS` — not appended, because the
file's tail is inside `@media (max-width: 480px)`. Responsive adjustments are
added to the existing 768/640/480 blocks.

Tokens only, no raw hex. `aspect-ratio: 16 / 9` on the video wrapper.

**Acceptance criteria:**
- [ ] New rules sit above line 1506, outside every media query
- [ ] No raw hex values — `:root` tokens only
- [ ] Video holds 16:9 at 320px, 768px, 1440px
- [ ] No horizontal page scroll at 320px

**Verification:**
- [ ] `awk 'NR<1506' css/style.css | grep -c "episode"` → non-zero
- [ ] `grep -nE "#[0-9a-fA-F]{3,6}" css/style.css | awk -F: '$1>1490'` → no new hits
- [ ] DevTools device toolbar at 320 / 768 / 1440

**Dependencies:** Task 3
**Files:** `css/style.css`
**Scope:** S

---

### Checkpoint: Page complete
- [ ] `/webcast/` renders correctly at 320px, 768px, 1440px
- [ ] Video plays on click, silent on load
- [ ] Duplicate the episode block 3× locally — layout holds — then revert
- [ ] **Review with Gunnar before wiring the root page**

---

### Phase 3: Wire-up and documentation

#### Task 5: Link `/webcast/` from the root page

**Description:** Add `<li><a href="/webcast/">Webcast</a></li>` to the nav in
`index.html` and a matching entry to the footer links. **No content section is
added to the home page** — the 2027 page stays focused on ticket conversion.

**Acceptance criteria:**
- [ ] Nav shows Webcast between Speakers and Programme
- [ ] Footer links to `/webcast/`
- [ ] No other change to `index.html` — no new `<section>`
- [ ] Nav does not wrap or overflow at 375px

**Verification:**
- [ ] `git diff --stat index.html` → a small diff, additions only
- [ ] Click both links from `localhost:8000`
- [ ] Check nav at 375px and 768px

**Dependencies:** Task 2
**Files:** `index.html`
**Scope:** XS

---

#### Task 6: Document "Add a webcast episode" in README

**Description:** New numbered section under *How to update the site*, matching
the voice of the existing entries, plus `webcast/` and `assets/webcast/` in the
File structure tree. Must be followable by a non-developer: copy the block, edit
five fields, strip `autoPlay`, put newest first, paste the Spotify URL when the
show launches.

**Acceptance criteria:**
- [ ] Section numbered consistently with existing ones
- [ ] Explicitly warns to remove `autoPlay=1`
- [ ] Explicitly states newest episode goes first
- [ ] File structure tree includes `webcast/` and `assets/webcast/`

**Verification:**
- [ ] Read it start to finish as someone who has never seen the repo
- [ ] Every filename mentioned actually exists

**Dependencies:** Tasks 3, 4
**Files:** `README.md`
**Scope:** XS

---

#### Task 7: Full verification pass and deploy

**Description:** Run the SPEC.md testing checklist end to end, then push.

**Acceptance criteria:**
- [ ] All nine SPEC.md success criteria demonstrably met
- [ ] No `.nojekyll` file exists at the repo root
- [ ] `SPEC.md` still listed in `_config.yml` `exclude`

**Verification:**
- [ ] `grep -rn "autoPlay" webcast/` → nothing
- [ ] `ls -a | grep nojekyll` → nothing
- [ ] Tab through `/webcast/`; focus visible on every interactive element
- [ ] Click every link on the page
- [ ] After push: `analyticsdev.net/webcast/` live; `analyticsdev.net/SPEC.md` 404s

**Dependencies:** Tasks 1–6
**Files:** none (verification only)
**Scope:** XS

---

### Checkpoint: Complete
- [ ] All SPEC.md success criteria met
- [ ] Live at `analyticsdev.net/webcast/`
- [ ] Internal docs absent from the live site

---

## Risks and Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| TwentyThree blocks cross-origin framing | **High** — kills the embed design | Task 1 resolves it first; thumbnail-card fallback ready |
| New CSS appended to file tail, silently scoped to `@media (max-width: 480px)` | **High** — styles work on phone, break on desktop; easy to miss | Insertion point pinned to before line 1506; Task 4 verifies with `awk` |
| `autoPlay=1` survives a future copy-paste | Medium | Stripped in markup, warned in the EDIT comment, warned in README, grep in Task 7 |
| A `.nojekyll` file gets added later, publishing SPEC.md and onboarding.md | Medium | Already warned in README; re-checked in Task 7 |
| Spotify URL never gets pasted, pending state becomes permanent | Low | Pending line states a fact rather than promising a date; no dead link either way |
| Absolute `/webcast/` links appear broken under VS Code Live Preview | Low | Known, documented in README; use `python3 -m http.server` |
| Nav overflows on mobile with a fifth item | Low | Checked at 375px in Task 5 |

---

## Parallelization

Small enough to run sequentially, and sequential is the right call — Tasks 2, 3,
and 4 all touch `webcast/index.html` or its styling. Task 5 (`index.html`) and
Task 6 (`README.md`) touch disjoint files and could run alongside the main
chain, but the coordination cost exceeds the saving at this size.

**Do not parallelize Tasks 2–4.** They are one file being built in three
verifiable steps.

---

## Open Questions

Carried from SPEC.md. Only #1 blocks a task; the rest have safe defaults.

1. **Episode 1 broadcast date and description** — blocks Task 3 from shipping
   final copy. Placeholder otherwise.
2. **Guest thumbnail** — reuse `assets/speakers/2027/simo-ahava.jpg`, or a still
   from the recording? Defaults to reuse; `assets/webcast/` is only created if a
   new image is supplied.
3. **TwentyThree framing** — Task 1 closes this.
4. **Spotify show-level URL** — arriving later this month; may warrant a link in
   the series blurb, separate from per-episode links.
5. **Backlinks from BLC and Spotify show notes to `/webcast/`** — outside this
   repo, worth coordinating.
