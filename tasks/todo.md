# TODO: Webcast Series page

Working checklist for [plan.md](plan.md), implementing [SPEC.md](../SPEC.md).
Tick as you go. Do not start a task before its dependencies are ticked.

---

## Phase 1 — Resolve the risk

- [ ] **Task 1 — Confirm the TwentyThree player can be framed** · XS · deps: none
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

- [ ] **Task 2 — Create `webcast/index.html` skeleton** · S · deps: 1
  - Acceptance: renders correctly using only existing CSS classes; nav id is
    `nav-links-webcast`; mobile toggle works; headings nest h1→h2
  - Verify: `python3 -m http.server 8000` → `/webcast/`; toggle nav at 375px;
    `grep -c "GTM-5Z4PKJ8L" webcast/index.html` → `1`
  - Files: `webcast/index.html`

- [ ] **Task 3 — Add the episode 1 block** · S · deps: 2
  - Acceptance: video plays on click, silent on load; Spotify slot is a muted
    pending line, not a dead link; every editable field has an `EDIT` comment
  - Verify: `grep -n "autoPlay" webcast/index.html` → no matches; load with
    sound on
  - Files: `webcast/index.html`
  - ⚠️ Blocked on real broadcast date + description (open question 1)

- [ ] **Task 4 — Add the `WEBCAST SERIES` CSS section** · S · deps: 3
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

- [ ] **Task 5 — Link `/webcast/` from the root page** · XS · deps: 2
  - Acceptance: nav + footer links added; **no new section** on `index.html`;
    nav does not wrap at 375px
  - Verify: `git diff --stat index.html` shows a small additions-only diff;
    click both links
  - Files: `index.html`

- [ ] **Task 6 — Document "Add a webcast episode" in README** · XS · deps: 3, 4
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

- [ ] Episode 1 broadcast date + 1–2 sentence description → blocks Task 3
- [ ] Guest thumbnail: reuse `assets/speakers/2027/simo-ahava.jpg`, or new still?
- [ ] Spotify show URL (launching later this month) → pending state until then
