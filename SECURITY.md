# Security Policy

## Reporting a Vulnerability

If you discover a security issue (exposed secret, vulnerable dependency, CI
injection, etc.) in this repository, please **do not open a public issue**.

Contact the repository owner directly:
- GitHub: [@SkyBeamProject](https://github.com/SkyBeamProject)
- Use [GitHub's private vulnerability-reporting feature](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability)
  on this repository (Security → Report a vulnerability).

We aim to respond within **72 hours**.

---

## Incident-Response Checklist

Use this checklist if you believe the repository or associated accounts have
been compromised ("consider me hacked" scenario).

### 1 — Contain: lock down access immediately

- [ ] **Revoke all personal access tokens (PATs)** for your GitHub account:
  Settings → Developer settings → Personal access tokens → Revoke all suspicious tokens.
- [ ] **Rotate any exposed secrets** in GitHub Secrets:
  Repo → Settings → Secrets and variables → Actions → delete/recreate every secret.
- [ ] **Review OAuth app authorisations**: Settings → Applications → Authorised OAuth Apps.
- [ ] **Review GitHub App installations**: Settings → Applications → Installed GitHub Apps.
- [ ] **Change your GitHub account password** and ensure 2-FA (TOTP or hardware key) is active.
- [ ] If a deploy key was in the repo, rotate it: Settings → Deploy keys.

### 2 — Assess: understand what was exposed

- [ ] Review the last 30 commits on `main` for unexpected files or script
  injections (`git log --oneline -30`).
- [ ] Check `.github/workflows/` for any new or modified steps that could
  exfiltrate secrets or install malware.
- [ ] Audit GitHub Actions run logs for the last 30 days:
  Actions tab → select workflow → check each run's output.
- [ ] Scan the full git history for secrets:
  ```bash
  # Install truffleHog or gitleaks, then run:
  gitleaks detect --source . --verbose
  # or
  trufflehog git file://. --only-verified
  ```
- [ ] Search for high-entropy strings and common secret patterns:
  ```bash
  grep -rn "ghp_\|AKIA\|sk-\|-----BEGIN" . --include="*.py" --include="*.yml" \
       --include="*.json" --include="*.env"
  ```

### 3 — Purge: remove sensitive data from history

> ⚠️ This rewrites history. Coordinate with all collaborators first.

#### Remove a file or directory from the entire git history

```bash
# Using git-filter-repo (recommended):
pip install git-filter-repo
git filter-repo --path "Presumed Personal Government Digital Database" --invert-paths
git filter-repo --path "Personal Predicament" --invert-paths
git push origin --force --all
git push origin --force --tags
```

After force-pushing, **every collaborator must re-clone** the repository.

#### Invalidate GitHub's cached views

Contact GitHub Support to request that cached/archived copies of removed
content are purged:
<https://support.github.com/contact>

### 4 — Harden: prevent recurrence

- [ ] Enable **GitHub Secret Scanning** and **Push Protection**:
  Settings → Code security → Secret scanning → Enable.
- [ ] Enable **Dependabot alerts** and **Dependabot security updates**:
  Settings → Code security → Dependabot → Enable both.
- [ ] Review and restrict repository visibility if sensitive content exists.
- [ ] Ensure Actions workflow permissions are minimal (see below).
- [ ] Pin all third-party GitHub Actions to a specific commit SHA.
- [ ] Add branch-protection rules to `main`:
  - Require pull-request reviews before merging.
  - Require status checks to pass.
  - Disallow force pushes.
  - Restrict who can push directly.

---

## Sensitive Data in This Repository

### Known sensitive directories

The following directories **contain personally-identifiable documents** (government
IDs, forms, driver's licence scan) that were unintentionally committed to this
public repository:

| Directory | Contents |
|---|---|
| `Presumed Personal Government Digital Database/` | Slovenian government identity documents, forms, and driver's licence scan |
| `Personal Predicament/` | Personal situational records |

**These directories are now excluded from the PDF→Markdown CI pipeline** via
`tools/pdf_to_md/convert.py` to prevent further automated re-publishing as
readable text.

**They must still be purged from git history** using the steps in section 3
above. Until that purge is completed:
- The raw files remain accessible via the GitHub web UI and `git clone`.
- Anyone who has cloned the repository before the purge retains the files.
- Consider making the repository **private** immediately until the purge is done.

### Secret rotation steps (no secrets included here)

If any credentials, tokens, or keys were found in the repository:

1. **GitHub Personal Access Tokens**: Revoke at Settings → Developer settings → Personal access tokens.
2. **GitHub Actions Secrets**: Delete and recreate at Settings → Secrets and variables → Actions.
3. **AWS keys (`AKIA…`)**: Deactivate in the IAM console, then delete. Create a new key pair.
4. **OpenAI / API keys (`sk-…`)**: Revoke at the provider's dashboard; generate a new key.
5. **SSH private keys (`-----BEGIN … PRIVATE KEY-----`)**: Generate a new key pair; remove the old public key from all authorised hosts.
6. **Assume any exposed credential is compromised** — rotate it immediately, even if you are not certain it was accessed.

---

## GitHub Actions Security

This repository's CI workflow (`.github/workflows/pdf-to-md.yml`) follows these
security practices:

- **Minimum permissions**: `contents: read` at workflow level; `contents: write`
  scoped only to the convert job that must push generated Markdown.
- **Pinned actions**: All `uses:` references are pinned to a specific commit SHA
  with a `# vX.Y.Z` comment indicating the corresponding version tag.
- **No secrets in steps**: The workflow does not consume any repository secrets.
- **`[skip ci]`**: Auto-commits include `[skip ci]` to avoid infinite loops.

---

## Recommended Tools

| Tool | Purpose |
|---|---|
| [gitleaks](https://github.com/gitleaks/gitleaks) | Scan git history for secrets |
| [truffleHog](https://github.com/trufflesecurity/trufflehog) | Deep secret scanning with entropy analysis |
| [git-filter-repo](https://github.com/newren/git-filter-repo) | Rewrite history to remove files |
| [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-scanning) | Automated secret detection (free for public repos) |
| [Dependabot](https://docs.github.com/en/code-security/dependabot) | Dependency vulnerability alerts |
