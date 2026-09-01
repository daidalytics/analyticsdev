# TODO: Webcast Series page

Working checklist for [plan.md](plan.md), implementing [SPEC.md](../SPEC.md).
Tick as you go. Do not start a task before its dependencies are ticked.

---

## Phase 1 — Resolve the risk

- [x] **Task 1 — Confirm the TwentyThree player can be framed** · XS · deps: none
      _Resolved: Gunnar supplied the platform’s own Share→Embed code (`source=embed`), so framing is intended. Visual confirm still worthwhile._
  - Acceptance: player renders and plays from a local test file, or a specific
    console refusal is captured
  - Verify: no `X-Frame-Options` / `frame-ancestors` error in DevTools console
  - Files: scratchpad only
  - If blocked: **stop and report.** Fall back to a link-out thumbnail card.

### ⛔ Checkpoint — risk resolved
- [ ] Framing works, or fallback approved by Gunnar
- [ ] SPEC.md open question 3 closed

---

## Phase 2 — The page

- [x] **Task 2 — Create `webcast/index.html` skeleton** · S · deps: 1
      _Done, commit `0a8b9ef`. All 21 CSS classes used already existed — the
      skeleton needed no new styling, confirming Task 4 is episode-only._
  - Acceptance: renders correctly using only existing CSS classes; nav id is
    `nav-links-webcast`; mobile toggle works; headings nest h1→h2
  - Verify: `python3 -m http.server 8000` → `/webcast/`; toggle nav at 375px;
    `grep -c "GTM-5Z4PKJ8L" webcast/index.html` → `1`
  - Files: `webcast/index.html`

- [x] **Task 3 — Add the episode 1 block** · S · deps: 2
      _Done. Simo Ahava, 31 Aug 2026. No autoplay param in the src._
  - Acceptance: video plays on click, silent on load; Spotify slot is a muted
    pending line, not a dead link; every editable field has an `EDIT` comment
  - Verify: `grep -n "autoPlay" webcast/index.html` → no matches; load with
    sound on
  - Files: `webcast/index.html`
  - ⚠️ Blocked on real broadcast date + description (open question 1)

- [x] **Task 4 — Add the `WEBCAST SERIES` CSS section** · S · deps: 3
      _Done. 11 rules above the media queries, 0 stranded, tokens only._
  - Acceptance: rules sit **before line 1506**, outside every media query;
    tokens only, no raw hex; video holds 16:9; no horizontal scroll at 320px
  - Verify: `awk 'NR<1506' css/style.css | grep -c "episode"` → non-zero;
    DevTools at 320 / 768 / 1440
  - Files: `css/style.css`
  - ⚠️ The stylesheet ends **inside** `@media (max-width: 480px)`. Appending to
    the end of the file scopes the new rules to phones only.

### ⛔ Checkpoint — page complete
- [ ] Renders at 320px, 768px, 1440px
- [ ] Video plays on click, silent on load
- [ ] Duplicate the episode block 3× — layout holds — then revert
- [ ] **Review with Gunnar before wiring the root page**

---

## Phase 3 — Wire-up and documentation

- [x] **Task 5 — Link `/webcast/` from the root page** · XS · deps: 2
      _Done, commit `0a8b9ef`. 4-line additions-only diff; no new section._
  - Acceptance: nav + footer links added; **no new section** on `index.html`;
    nav does not wrap at 375px
  - Verify: `git diff --stat index.html` shows a small additions-only diff;
    click both links
  - Files: `index.html`

- [x] **Task 6 — Document "Add a webcast episode" in README** · XS · deps: 3, 4
      _Done, section 6._
  - Acceptance: numbered consistently; warns to strip `autoPlay=1`; states
    newest-first; file tree updated with `webcast/`
  - Verify: read it as a first-time reader; every filename mentioned exists
  - Files: `README.md`

- [ ] **Task 7 — Full verification pass and deploy** · XS · deps: 1–6
  - Acceptance: all nine SPEC.md success criteria met; no `.nojekyll`; `SPEC.md`
    still in `_config.yml` exclude
  - Verify: `grep -rn "autoPlay" webcast/` → nothing; `ls -a | grep nojekyll` →
    nothing; tab through the page; after push `analyticsdev.net/webcast/` is
    live and `analyticsdev.net/SPEC.md` 404s
  - Files: none

### ⛔ Checkpoint — complete
- [ ] All success criteria met
- [ ] Live at `analyticsdev.net/webcast/`
- [ ] Internal docs absent from the live site

---

## Blocked on Gunnar

- [ ] **Visual check of `/webcast/`** — `python3 -m http.server 8000`, open
      `/webcast/`, confirm the video renders and stays silent until clicked →
      last gate before Task 7's push
- [ ] **`allow="autoplay"` on the iframe** — kept as supplied in the Share→Embed
      code. It grants permission but does not trigger playback; drop the word
      `autoplay` from the attribute if you want it impossible rather than
      merely unused.
- [ ] Guest thumbnail: reuse `assets/speakers/2027/simo-ahava.jpg`, or new still?
      Not currently used — the page leads with the video instead.
- [ ] Spotify show URL (launching later this month) → pending state until then

~~Episode 1 date + description~~ — supplied 1 Sep 2026.
~~Framing spike~~ — resolved by the official embed code.
