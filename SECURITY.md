# Security & Incident Response

> "It is what it is" — acknowledged.  
> This note exists so there is a clear, calm playbook if repositories disappear or account access is lost again.

---

## Emergency: Repositories Disappeared

### Step 1 — Check your session first

1. Open GitHub in a **private / incognito** browser window.
2. Sign in and confirm the username at the top-right is exactly **SkyBeamProject**.
3. Visit `https://github.com/SkyBeamProject?tab=repositories`

If the repos reappear here, the issue was a session or wrong-account mix-up — nothing was deleted.

---

### Step 2 — Test one missing repo by direct URL

Type the exact URL of a repo you know existed.

| Result | Meaning |
|---|---|
| **404 Not Found** | Deleted, transferred, made private, or not logged in correctly |
| **403 / "You don't have access"** | Repo still exists — your permissions were removed |
| **Repo loads normally** | Visibility or filter issue in the list view |

This one answer determines every next step.

---

### Step 3 — Lock down the account (do this now, even if unsure)

1. **Change your GitHub password** — use a unique password of at least 16 characters. A password manager (e.g. Bitwarden, 1Password) can generate and store one safely.
2. **Enable or verify Two-Factor Authentication (2FA)**  
   Settings → *Password and authentication* → enable an authenticator app.
3. **Revoke anything you do not recognise:**
   - Settings → *Applications* → remove unknown **OAuth Apps** and **GitHub Apps**
   - Settings → *SSH and GPG keys* → delete unknown SSH keys
   - Settings → *Developer settings → Personal access tokens* → revoke unknown tokens; rotate the ones you still use
4. If you use **GitHub Actions** in any repo: rotate all repository and organisation secrets.

---

### Step 4 — Check logs and email alerts

**Your email inbox** — search for GitHub messages with these subjects:
- "Repository deleted"
- "Repository transferred"
- "Repository visibility changed"
- "New sign-in to your account"
- "Two-factor authentication disabled"

**GitHub security log:**  
Settings → *Security log* — look for entries such as `repo.destroy`, `repo.transfer`, `org.remove_member`, `account.login` from unknown locations.

---

### Step 5 — Recovery paths

| Situation | Action |
|---|---|
| Repo was **deleted** | Settings → *Repositories* → *Deleted repositories* (if visible). If not there, open **GitHub Support** immediately — GitHub may be able to restore recently-deleted repos, but the window varies by account and plan, so contact Support as soon as possible for the accurate timeline. |
| Repo was **transferred** | Check your email for a transfer notice. Old URLs may redirect or show 404. Support can assist if the transfer was unauthorised. |
| Account or org is **restricted / suspended** | Only GitHub Support can restore this. Gather the exact times and any emails you received, then open a support ticket. |
| You lost **org owner access** | Ask another owner to re-add you, or contact GitHub Support with proof of ownership. |

**GitHub Support:** https://support.github.com

---

### Step 6 — Local backup guidance (for the future)

If you have any repo cloned locally, protect it right now:

```bash
# Create a full mirror backup (single file, contains all history)
git bundle create repo-backup.bundle --all

# Or create a complete mirror clone (keeps all branches and tags)
git clone --mirror https://github.com/SkyBeamProject/<repo-name>.git
```

Store these files on an external drive or cloud storage separate from GitHub.

**To restore a bundle later:**
```bash
git clone repo-backup.bundle restored-repo
```

**To restore a mirror clone later:**
```bash
git clone --local <mirror-folder>.git restored-repo
```

Running one of these for each important repo takes only a few minutes and means you always have a copy regardless of what happens to GitHub.

---

### Quick summary checklist

- [ ] Logged in as the correct account in a fresh browser window
- [ ] Tested a missing repo by direct URL (got 404 or 403?)
- [ ] Changed GitHub password
- [ ] 2FA is enabled
- [ ] Revoked unknown OAuth apps, GitHub Apps, SSH keys, tokens
- [ ] Checked email for deletion / transfer / visibility-change notices
- [ ] Checked GitHub security log
- [ ] Opened GitHub Support ticket if repos are still missing
- [ ] Created local `.bundle` or `--mirror` backups going forward
