# Contributing to This Repository

## Working with Git: A Beginner-Friendly Guide

This guide explains Git terminology used in this repository and how to contribute safely.

---

### The `main` Branch

**What it is**
- `main` is the default branch of this repository — the stable, authoritative version of all documents and code.
- It is the branch that GitHub shows first when you visit the repository page.
- All reviewed and accepted contributions are eventually merged here.

**Why it exists**
- It provides a single source of truth.
- It protects the corpus from unreviewed or experimental edits.
- Automated workflows (e.g., the PDF-to-Markdown converter) run against `main`.

**`main` vs `master`**
- Older Git repositories used `master` as the default branch name. GitHub now defaults to `main` for new repositories.
- This repository uses `main`. To confirm the default branch of any repository:

```bash
# On the command line
git remote show origin | grep "HEAD branch"

# Or check the GitHub repository page — the default branch is shown in the branch selector.
```

---

### Feature Branches

Never commit experimental or draft changes directly to `main`. Instead:

1. **Create a feature branch** off `main`:

```bash
git switch main
git pull origin main
git switch -c feature/your-descriptive-name
```

2. **Make your changes** on the feature branch.

3. **Push the branch** to GitHub:

```bash
git push origin feature/your-descriptive-name
```

4. **Open a Pull Request (PR)** on GitHub targeting `main`. This triggers review before any merge.

---

### Common Git Commands (High-Level)

| Command | Purpose |
|---------|---------|
| `git switch <branch>` | Switch to an existing branch (preferred over `git checkout` for branch navigation) |
| `git checkout <branch>` | Older equivalent of `git switch`; also used to restore individual files |
| `git pull origin main` | Fetch remote changes and merge them into your current branch |
| `git fetch origin` | Download remote changes without applying them; safe to run at any time |
| `git merge <branch>` | Merge another branch into your current branch, creating a merge commit |
| `git rebase main` | Replay your branch's commits on top of `main`, producing a linear history |

**When to use `merge` vs `rebase`**
- Use `merge` for integrating completed feature branches (preserves context).
- Use `rebase` to keep a feature branch up to date with `main` before opening a PR (cleaner history).
- Never rebase commits that have already been pushed to a shared branch.

---

### Quick Workflow Summary

```bash
# Start a new piece of work
git switch main && git pull origin main
git switch -c feature/add-new-document

# ...edit files...

git add .
git commit -m "docs: add new document on X"
git push origin feature/add-new-document

# Open a Pull Request on GitHub → base: main
```

---

### Glossary

| Term | Meaning in this repository |
|------|---------------------------|
| **main** | The default, primary integration branch of this repository |
| **feature branch** | A short-lived branch created for a specific change, merged back to `main` via PR |
| **PR (Pull Request)** | A GitHub mechanism to review and discuss changes before merging into `main` |
| **default branch** | The branch GitHub displays and uses as the target for PRs — `main` here |
| **HEAD** | A pointer to the commit you currently have checked out |
| **origin** | The conventional alias for this repository's remote URL on GitHub |
| **explain away** | Informal rhetorical term meaning to dismiss or account for an apparent inconsistency. Not a Git or repository-specific command; if encountered in a document it is used in its ordinary English sense. |
