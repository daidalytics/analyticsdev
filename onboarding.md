# Onboarding — how to edit the AnalyticsDev website

**Who this is for:** anyone at BLC who needs to keep [analyticsdev.net](https://analyticsdev.net)
up to date. It assumes **no technical background at all**. You do not need to know how
to code. If you can edit a Word document and follow instructions carefully, you can do this.

Set aside about 45 minutes for the one-time setup. After that, a typical change
(adding a speaker, updating a date) takes 5–10 minutes.

**Read this first, then keep [README.md](README.md) open as your reference** — this
document teaches you the tools; the README lists the specific things you'll edit.

---

## Contents

- [Part 0 — How the website works (5 min read)](#part-0--how-the-website-works)
- [Part 1 — Set up your GitHub account](#part-1--set-up-your-github-account)
- [Part 2 — The easy path: edit in your browser](#part-2--the-easy-path-edit-in-your-browser)
- [Part 3 — Your first real change, step by step](#part-3--your-first-real-change-step-by-step)
- [Part 4 — The full setup: VS Code on your computer](#part-4--the-full-setup-vs-code-on-your-computer)
- [Part 5 — Common tasks](#part-5--common-tasks)
- [Part 6 — Rules and safety net](#part-6--rules-and-safety-net)
- [Part 7 — When something goes wrong](#part-7--when-something-goes-wrong)
- [Glossary](#glossary)

---

## Part 0 — How the website works

Three things to understand before you touch anything.

### 1. The website is just files

There is no CMS, no WordPress, no login-and-click admin panel. The entire site is a
handful of text files sitting in a folder. The most important one is `index.html` —
that single file contains almost everything you see on the homepage: the dates, the
speakers, the programme, the sponsor logos.

To change the website, you change the text in that file. That's it.

### 2. GitHub is where the files live

GitHub is like Google Drive, but built for files like these. It stores the master
copy, keeps a complete history of every change ever made, and shows who changed what
and when.

The folder is called a **repository** (or "repo"). Ours is:

> **https://github.com/daidalytics/analyticsdev**

### 3. Saving to GitHub publishes the website

This is the part that surprises people. There is no separate "publish" button.

```
You edit index.html  →  You save it to GitHub  →  GitHub Pages rebuilds the site
                                                   →  analyticsdev.net is updated
                                                      (takes 1–2 minutes)
```

The service doing that last step is called **GitHub Pages**. It watches the repository
and automatically serves whatever is in it as a live website.

**So: saving = publishing.** Take that seriously, but don't be scared of it — every
change is reversible, and Part 6 explains how.

### The words you'll see

You only need four, and they all describe the same one action:

| Word | What it actually means |
| ---- | ---------------------- |
| **Commit** | Save your change, with a short note explaining what you did |
| **Push** | Send your saved change up to GitHub |
| **Branch** | A named version of the files. Ours is called `main` — the live one |
| **Repository** | The folder holding the website |

In the browser editor, commit and push happen together in one click. See the
[Glossary](#glossary) at the end for anything else you bump into.

---

## Part 1 — Set up your GitHub account

### 1.1 Create the account

1. Go to **[github.com/signup](https://github.com/signup)**
2. Enter your **work email address** (use your BLC address, not a personal one — it
   keeps ownership clear if someone leaves)
3. Choose a password and a username. The username is public and appears next to every
   change you make. Something like `firstname-blc` or your name is fine. Keep it
   professional — it's visible on the public repository.
4. Verify your email address when the confirmation mail arrives
5. Choose the **Free** plan when offered. Everything we need is free.

### 1.2 Turn on two-factor authentication (required)

GitHub requires this, and it protects the live website. Do it now, not later.

1. Click your **profile picture** (top right) → **Settings**
2. In the left sidebar: **Password and authentication**
3. Under **Two-factor authentication**, click **Enable two-factor authentication**
4. Choose **authenticator app** and scan the QR code with Google Authenticator,
   Microsoft Authenticator, or 1Password
5. **Save the recovery codes somewhere safe** — a password manager, or print them.
   Without them, losing your phone means losing access to your account.

### 1.3 Get access to the repository

Send your GitHub **username** (not your email) to Gunnar or whoever currently
administers the `daidalytics` account, and ask to be added as a collaborator on the
`analyticsdev` repository.

You'll get an email invitation. **Click the link and accept it** — the invitation
expires after 7 days.

**How to check it worked:** go to
[github.com/daidalytics/analyticsdev](https://github.com/daidalytics/analyticsdev).
If you can see a **pencil icon (✏️)** when you open a file, you have edit access. If
you only see a "Fork" button and no pencil, the invitation hasn't been accepted yet.

---

## Part 2 — The easy path: edit in your browser

**You can do 90% of the work without installing anything.** GitHub has a full editor
built into the website. Start here. Only move to Part 4 if you want to preview changes
before they go live.

### Opening the editor

1. Go to [github.com/daidalytics/analyticsdev](https://github.com/daidalytics/analyticsdev)
2. Press the **`.`** key (full stop) on your keyboard

That's it. A complete code editor opens in your browser at `github.dev`. It looks and
works exactly like VS Code, because it *is* VS Code — just running in a browser tab.

> Alternative if the `.` shortcut doesn't work: change `github.com` to `github.dev` in
> the address bar and press Enter.

### What you're looking at

```
┌──────────────┬────────────────────────────────────────────┐
│  EXPLORER    │                                            │
│              │                                            │
│  > 2026      │      The file you're editing               │
│  > assets    │      appears here                          │
│  > css       │                                            │
│    index.html│                                            │
│    README.md │                                            │
│              │                                            │
└──────────────┴────────────────────────────────────────────┘
   ↑ Files                ↑ Editor
```

Click `index.html` in the left sidebar to open it.

### Finding what you need to change

`index.html` is around 700 lines long. **Do not read it top to bottom.** Every part
you're meant to edit is labelled with a marker that looks like this:

```html
<!-- EDIT: Update the Billetto href below when registration opens -->
```

Anything wrapped in `<!--` and `-->` is a **comment** — a note for humans that the
website ignores completely.

**To find them all:** press **Ctrl+F** (Windows) or **Cmd+F** (Mac) and search for
`EDIT:`. You'll get a list of every editable spot. There are around 30 of them.

### Saving (= publishing)

1. Make your edit
2. Click the **Source Control** icon in the far-left bar — it looks like a branching
   line, and shows a small blue badge with the number of changed files
3. Type a short message in the box saying what you changed, e.g.
   `Add Julius Fedorovicius to speakers`
4. Click **Commit & Push**

Your change is live at analyticsdev.net within about 1–2 minutes. Hard-refresh the
page (**Ctrl+Shift+R** / **Cmd+Shift+R**) if you still see the old version.

---

## Part 3 — Your first real change, step by step

Let's do something small and safe so the whole loop makes sense. We'll fix the
copyright year in the footer.

**1.** Open [github.com/daidalytics/analyticsdev](https://github.com/daidalytics/analyticsdev)
and press **`.`**

**2.** Click `index.html` in the left sidebar

**3.** Press **Ctrl+F** / **Cmd+F** and search for `EDIT: Update copyright year`

**4.** Just below the marker you'll find a line with the year in it. Click into it and
change the number.

**5.** Click the **Source Control** icon (left bar, branching-line symbol)

**6.** In the message box, type: `Update copyright year`

**7.** Click **Commit & Push**

**8.** Wait 1–2 minutes, then open [analyticsdev.net](https://analyticsdev.net) and
scroll to the bottom. Hard-refresh if needed.

You just deployed a website. The loop is always the same: **open → find the EDIT
marker → change the text → commit & push**.

### Watching the deploy

If you want to see it happen: on the repository page, click the **Actions** tab. Each
push appears as a row.

- 🟡 Yellow dot — building right now
- ✅ Green tick — live
- ❌ Red cross — something failed (see [Part 7](#part-7--when-something-goes-wrong))

---

## Part 4 — The full setup: VS Code on your computer

**Skip this section unless you want to preview changes before publishing.** The
browser editor from Part 2 is enough for most work.

The advantage of the local setup: you can see exactly how the page looks *before*
anyone else does. Worth it if you're making a bigger change, like restructuring the
programme.

### 4.1 Install VS Code

**VS Code** (Visual Studio Code) is a free text editor from Microsoft. It is the same
editor as `github.dev`, just installed on your machine.

1. Go to **[code.visualstudio.com](https://code.visualstudio.com)**
2. The big blue button detects your operating system — click it
3. **Mac:** open the downloaded `.zip`, then drag `Visual Studio Code` into your
   `Applications` folder
   **Windows:** run the downloaded `.exe` and accept the defaults. Tick **"Add to
   PATH"** if offered.
4. Open it. Skip or accept the welcome screens.

### 4.2 Install GitHub Desktop

**GitHub Desktop** handles the syncing between your computer and GitHub, with buttons
instead of typed commands. It exists precisely so you don't have to learn the command
line.

1. Go to **[desktop.github.com](https://desktop.github.com)**
2. Download and install it
3. Open it and click **Sign in to GitHub.com**
4. Your browser opens — approve the login, and confirm your two-factor code
5. When asked for a name and email for your commits, use your real name and your BLC
   email address

### 4.3 Download the website to your computer

In GitHub Desktop:

1. **File → Clone repository**
2. Open the **GitHub.com** tab — `daidalytics/analyticsdev` should be listed. If it
   isn't, your invitation from step 1.3 hasn't been accepted.
3. Choose where to save it. The default (`Documents/GitHub/analyticsdev`) is fine —
   just remember it.
4. Click **Clone**

"Cloning" = downloading your own full copy, including the entire history.

### 4.4 Open it in VS Code

In GitHub Desktop, click **Open in Visual Studio Code**. (If prompted, choose VS Code
as your external editor.)

You now have all the site files in front of you, same layout as Part 2.

### 4.5 Preview the site locally

This is the reason you did all this. You'll see the site running on your own machine
at an address only you can reach.

**In VS Code:** install the Live Preview extension once —

1. Click the **Extensions** icon in the left bar (four small squares)
2. Search for **`Live Preview`** (publisher: Microsoft)
3. Click **Install**

Then, any time you want to preview: **right-click `index.html`** in the sidebar →
**Show Preview**. The page opens inside VS Code and **refreshes automatically as you
type**. Nothing is published — this is entirely on your computer.

> **Why not just double-click the HTML file?** You can, and it mostly works, but some
> paths and links behave differently than they will on the real server. Live Preview
> is closer to the truth.

### 4.6 The daily rhythm

Four steps, every time:

**1. Pull first.** Open GitHub Desktop and click **Fetch origin**, then **Pull** if it
offers. This grabs anything other people changed. *Do this before you start editing,
every time* — it prevents the most common headache.

**2. Edit** in VS Code. Save with **Ctrl+S** / **Cmd+S**. Saving here only saves to
your computer — nothing is published yet.

**3. Commit.** Switch to GitHub Desktop. Your changes are listed on the left, with
old and new versions shown side by side. At the bottom left, type a summary
(`Add Kristina von der Bank bio`) and click **Commit to main**.

**4. Push.** Click **Push origin** at the top. *Now* it's live, in 1–2 minutes.

Steps 3 and 4 are the two halves of what the browser editor's "Commit & Push" button
does in one go.

---

## Part 5 — Common tasks

Each of these is documented in full in [README.md](README.md) — this is the short
version so you know what you're getting into.

### Update the event date, venue, or ticket link

Search `index.html` for `EDIT: Update date, venue`. Also update the `<title>` and
`<meta name="description">` near the very top of the file — those control what shows
in Google results and when the link is shared on LinkedIn.

**Difficulty:** easy. Pure text replacement.

### Add a speaker

Two parts.

**The photo:** add a square JPG or PNG to `assets/speakers/`. Name it
`firstname-lastname.jpg`, all lowercase, hyphens instead of spaces, no
special characters (`kristina-von-der-bank.png`, not `Kristina VD Bank.PNG`). Aim for
roughly 600×600 pixels and under 300 KB — larger files make the page slow.

*To upload in the browser editor:* drag the file from your desktop straight onto the
`assets/speakers` folder in the left sidebar.

**The card:** search for `EDIT: add new speaker tiles here`, copy an existing speaker
block from `<div class="speaker-card">` to its closing `</div>`, paste it, and change
the name, role, photo filename, bio, and session.

**Difficulty:** medium. Copy an existing block rather than typing one from scratch —
that's the whole trick.

### Update the programme

Search for `EDIT: Add, remove, or edit time slots`. Each row is a `<li>` block with a
time and a description. Copy, paste, edit.

Many entries currently say **`TBC`** — those are deliberate placeholders waiting for
real times.

**Difficulty:** medium.

### Add or change a sponsor logo

Add the logo to `assets/sponsors/` (SVG or PNG with a transparent background is best),
then search for `EDIT: Update Gold Partner` or
`EDIT: Add/remove Supporting Partner blocks`.

**Difficulty:** medium.

### Archive an event after it happens

This one has real sequencing to it — copying the current homepage into a year folder,
fixing all the file paths, then resetting the homepage for the next edition.

**Difficulty:** hard. **Ask Gunnar the first time.** Full steps are in
[README.md](README.md) under "Archive an event".

---

## Part 6 — Rules and safety net

### Never touch these

| File | Why |
| ---- | --- |
| `CNAME` | Contains `analyticsdev.net`. Deleting it takes the domain offline. |
| `css/style.css` | Controls the entire visual design. One typo can break every page. Ask first. |
| `favicon.ico`, `assets/favicon.svg` | Generated files — they have their own process. |
| Anything starting with `.` | Configuration. Ignore it. |

### Rules of thumb

**Change text, not structure.** Editing the words between `>` and `<` is always safe:

```html
<p class="speaker-name">Simo Ahava</p>
                        ^^^^^^^^^^ safe to change
```

The bits in angle brackets — `<p class="speaker-name">` — are structure. Leave them
alone unless you're copying a whole block.

**Copy, don't compose.** Need a new speaker card? Copy an existing one. Never write
HTML from scratch.

**Tags come in pairs.** Every `<div>` has a matching `</div>`. If you delete one, you
must delete the other. This is the single most common way to break the page.

**Special characters need escaping.** In HTML, `&` must be written as `&amp;`. So
"Arrival & Registration" becomes `Arrival &amp; Registration`. Same for `<` (`&lt;`)
and `>` (`&gt;`).

**One change at a time.** Make it, push it, check the live site, then start the next
one. If something breaks, you know exactly which change caused it.

**Never paste from Word.** Word replaces straight quotes with curly ones and inserts
invisible characters that break HTML. Paste into a plain text editor first (TextEdit
in plain-text mode, or Notepad), then copy from there.

### Everything is reversible

This is the important reassurance: **you cannot permanently break anything.** GitHub
keeps every version of every file forever.

**To see the history:** on the repository page, click **History** (or the clock icon
next to a file). Every change is there, with who made it and when.

**To undo the last change:**

1. Go to [github.com/daidalytics/analyticsdev/commits/main](https://github.com/daidalytics/analyticsdev/commits/main)
2. Click the commit you want to undo
3. Click the **`...`** menu (top right) → **Revert**
4. Confirm

GitHub creates a new change that reverses the old one. The site is back to normal in
1–2 minutes. Nothing is deleted — the history stays intact.

**If in doubt, ask before pushing rather than after.**

---

## Part 7 — When something goes wrong

### The site didn't update

- **Wait two more minutes.** Deploys aren't instant.
- **Hard-refresh:** Ctrl+Shift+R (Windows) / Cmd+Shift+R (Mac). Your browser caches
  the old version aggressively.
- **Try a private/incognito window** — that bypasses the cache entirely.
- **Check the Actions tab** on the repository. A red ❌ means the deploy failed.
- **Confirm you actually pushed.** In GitHub Desktop, a leftover "Push origin" button
  means your commit is still only on your computer.

### The page looks broken — text everywhere, layout collapsed

You almost certainly deleted or mistyped a tag. Two options:

1. **Undo it** using the Revert steps in Part 6. Always safe.
2. **Find it:** in VS Code, look for a wavy underline in the file, or check the
   **Problems** panel (**View → Problems**). It usually points straight at the line.

### A change I expected is missing / conflict warnings

Someone else edited the same file. In GitHub Desktop, click **Fetch origin** then
**Pull** to bring their work in. If you get a message about a **merge conflict**,
**stop and ask Gunnar** — don't try to resolve it by hand the first time.

Prevention: always pull before you start editing.

### I can't find the EDIT marker the README mentions

Two markers in the programme section are currently written as `<!- -` instead of
`<!--`. Search for just `EDIT:` rather than the full `<!-- EDIT:` and you'll find
everything.

### My image doesn't show up

- **Check the filename matches exactly**, including capitalisation and extension. On
  the live server, `Photo.JPG` and `photo.jpg` are different files, even though your
  Mac or Windows machine treats them as the same.
- **Check the path.** From the homepage it's `assets/speakers/name.jpg`. From inside
  the `2026/` folder it's `../assets/speakers/name.jpg` — the `../` means "go up one
  folder".

### I'm locked out of my GitHub account

Use the recovery codes you saved in step 1.2. If you didn't save them, contact GitHub
support — this can take days, which is why step 1.2 says to save them.

---

## Who to ask

| Question | Ask |
| -------- | --- |
| How do I edit X? | [README.md](README.md) first — it covers every editable section |
| Something is broken | Gunnar |
| Access / permissions | Gunnar (repository administrator) |
| Domain and DNS | Jens (administers the `analyticsdev.net` zone at Simply.com) |
| Content and copy | jomar@brandleadership.community |

---

## Glossary

**Branch** — A named version of the files. We only use one, called `main`, and it's
the live site.

**Clone** — Download your own full copy of the repository to your computer.

**Commit** — A saved change, with a short note describing it. Think "save point".

**Commit message** — The note attached to a commit. Write what you changed, not how:
`Add Olga Safonova to speakers`, not `updated file`.

**CNAME** — The file telling GitHub Pages that this repository should be served at
`analyticsdev.net`. Do not delete it.

**CSS** — The language controlling colours, fonts and layout. Lives in
`css/style.css`. Leave it alone unless you know what you're doing.

**DNS** — The system translating `analyticsdev.net` into a server address. Managed at
Simply.com, not on GitHub.

**Fetch / Pull** — Check for, and download, changes other people have made.

**GitHub Pages** — The free service turning this repository into a live website.

**HTML** — The language web pages are written in. It's tags (`<p>`, `<div>`) wrapping
content. That's all it is.

**Merge conflict** — Two people edited the same lines and GitHub can't decide which
wins. Ask for help.

**Push** — Send your commits up to GitHub. On this project, pushing publishes.

**Repository (repo)** — The folder containing the website and its full history.

**Revert** — Undo a previous commit by creating a new one that reverses it.

**Static site** — A website made of plain files, with no database or admin panel
behind it. Ours is one. It's why it's fast, free to host, and hard to break
permanently.

---

*Last updated: August 2026. If something here is wrong or unclear, fix it — this file
is edited exactly the same way as the website.*
