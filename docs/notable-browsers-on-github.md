# Notable Open-Source Web Browsers on GitHub

A curated reference list of open-source browsers and browser engines with a notable presence on GitHub.
Ordered roughly by breadth of impact and community size.
Where a project's primary source repository is elsewhere, that is noted.

---

## 1. WebKit
- **Description:** The browser engine powering Safari, most iOS browsers, and a range of embedded WebViews.
- **Repo:** https://github.com/WebKit/WebKit *(primary — Apple treats this GitHub repo as the canonical source)*
- **Why notable:** Foundational to the web; hundreds of contributors; used everywhere Apple operates and on many embedded platforms.

## 2. Servo
- **Description:** A browser engine written in Rust, originally started at Mozilla, now maintained as an independent Linux Foundation project.
- **Repo:** https://github.com/servo/servo *(primary)*
- **Why notable:** Pioneered safe, parallel layout via Rust; increasingly embedded in other projects (e.g., Verso browser, Tauri).

## 3. Ladybird
- **Description:** A greenfield, fully independent browser engine — not based on Chromium, Gecko, or WebKit — written in C++.
- **Repo:** https://github.com/LadybirdBrowser/ladybird *(primary)*
- **Why notable:** The first serious attempt in decades to build a browser engine from scratch; aims to break the engine monoculture.

## 4. Brave
- **Description:** A Chromium-based browser with built-in ad and tracker blocking, fingerprinting protection, and an optional crypto wallet.
- **Repo:** https://github.com/brave/brave-browser *(primary)*
- **Why notable:** One of the most-starred browser repos on GitHub; mainstream adoption; privacy focus without sacrificing compatibility.

## 5. Ungoogled Chromium
- **Description:** Chromium with all Google-specific integrations, services, and telemetry surgically removed via a patch set.
- **Repo:** https://github.com/ungoogled-software/ungoogled-chromium *(primary)*
- **Why notable:** Popular privacy choice for users who want Chromium's engine without Google's data collection; community-maintained patch approach.

## 6. qutebrowser
- **Description:** A keyboard-driven browser built on Qt WebEngine and Python, designed for power users who prefer not to touch the mouse.
- **Repo:** https://github.com/qutebrowser/qutebrowser *(primary)*
- **Why notable:** Vim-style keybindings; deeply configurable via a Python config file; strong following among terminal-centric users.

## 7. Nyxt
- **Description:** A keyboard-oriented browser whose entire interface and behaviour can be reprogrammed live in Common Lisp.
- **Repo:** https://github.com/atlas-engineer/nyxt *(primary)*
- **Why notable:** The "Emacs of browsers" — arbitrary extension and automation at a level no other browser exposes; unique design philosophy.

## 8. Vieb
- **Description:** A Vim-inspired browser built on Electron that supports full Vim motions, modes, and a vimrc-style config.
- **Repo:** https://github.com/Jelmerro/Vieb *(primary)*
- **Why notable:** Strict Vim parity (normal/insert/command/visual modes) in a modern, cross-platform package.

## 9. Min
- **Description:** A minimal, Electron-based browser with a focus on clarity — built-in ad blocker, reading list, and distraction-free layout.
- **Repo:** https://github.com/minbrowser/min *(primary)*
- **Why notable:** Lightweight and open; a clean example of what a browser can look like when stripped to essentials.

## 10. Otter Browser
- **Description:** A Qt-based browser explicitly modelled on the classic Opera 12.x interface and feature set.
- **Repo:** https://github.com/OtterBrowser/otter-browser *(primary)*
- **Why notable:** Preserves a UI paradigm (sidebar, session manager, notes, mail) that modern browsers abandoned; Qt cross-platform.

## 11. Falkon
- **Description:** A cross-platform browser using Qt and QtWebEngine, integrated into the KDE ecosystem (formerly QupZilla).
- **Repo:** https://github.com/KDE/falkon *(primary GitHub repo maintained by KDE)*
- **Why notable:** First-class Plasma desktop integration; lightweight alternative to Chromium/Firefox on KDE.

## 12. Pale Moon
- **Description:** A Firefox fork with its own Goanna engine (a Gecko derivative), focused on efficiency and preserving XUL/XPCOM extensions.
- **Repo:** https://github.com/MoonchildProductions/pale-moon *(note: Pale Moon's canonical source is also hosted at repo.palemoon.org; GitHub is a secondary mirror)*
- **Why notable:** Keeps alive older Firefox extension APIs and a lighter rendering path; own engine lineage diverged significantly from mainline Firefox.

## 13. w3m
- **Description:** A terminal-based text browser that renders tables, handles forms, and even displays inline images in capable terminals.
- **Repo:** https://github.com/tats/w3m *(active maintenance fork; original upstream is dormant)*
- **Why notable:** Fast, scriptable, SSH-friendly; a practical tool for reading docs and testing pages from the command line.

## 14. Kristall
- **Description:** A small, cross-platform browser that supports HTTP/HTTPS alongside alternative protocols: Gemini, Gopher, and FTP.
- **Repo:** https://github.com/MasterQ32/kristall *(primary)*
- **Why notable:** One of the few graphical browsers targeting the small-web / alternative-internet stack; useful for Gemini exploration.

## 15. gecko-dev (Firefox mirror)
- **Description:** A read-only GitHub mirror of Mozilla's Gecko engine — the core of Firefox.
- **Repo:** https://github.com/mozilla/gecko-dev *(mirror only — canonical source is Mozilla's Mercurial at hg.mozilla.org)*
- **Why notable:** High star and fork count; useful for browsing Firefox source without Mercurial. Issues and PRs are not accepted here; use Mozilla's Phabricator for contributions.

---

## Projects not on GitHub (notable, for completeness)

| Project | Engine | Primary source |
|---------|--------|----------------|
| Chromium | Blink + V8 | https://chromium.googlesource.com/chromium/src |
| Firefox | Gecko | https://hg.mozilla.org/mozilla-central |
| Tor Browser | Gecko (Firefox fork) | https://gitlab.torproject.org/tpo/applications/tor-browser |
| GNOME Web (Epiphany) | WebKitGTK | https://gitlab.gnome.org/GNOME/epiphany |
| NetSurf | LibNSWebKit | https://git.netsurf-browser.org/netsurf.git |

---

*Last updated: 2026-04-26. Repo URLs and primary-vs-mirror status verified at time of writing.*
