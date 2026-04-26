# Rok Bastl Main Folder
## A First-Principles Architecture for Post-Industrial Civilization

This repository is not a product, startup, or manifesto.
It is a systems-level exploration of energy, materials, governance,
consciousness, and survival under constraint.

### How to Read This Repository
- Start with `0 - INDEX.pdf`
- Then read `1 - Introduction.pdf`
- Use the 0–10 framework as a spine, not a sequence
- Technical documents are self-contained and cross-referenced

### What This Is
- A first-principles research corpus
- A design framework for resilient civilization
- A documented attempt to think without institutional constraints

### What This Is Not
- Not a political ideology
- Not a commercial proposal
- Not a medical prescription
- Not speculative fiction

### Status
This repository is:
- Partially complete
- Actively evolving
- Open to critique, not consensus

---

## Branching & Git Workflow

This section explains how to work with this repository using Git.
It uses simple language so that everyone, including non-native English speakers, can follow along.

### The `main` branch

- `main` is the **default branch** of this repository.
- It holds the most stable, up-to-date version of the project.
- All accepted changes are merged into `main`.
- GitHub shows `main` by default when you open the repository page.

---

### Step 1 — Get the latest `main`

Before starting any new work, make sure your local copy is up to date:

```bash
git switch main
git pull origin main
```

---

### Step 2 — Create a feature branch

Never work directly on `main`. Create a new branch for your change:

```bash
git switch -c feature/<your-branch-name>
# Example:
git switch -c feature/add-energy-section
```

Replace `<your-branch-name>` with a short, clear description of your work.

---

### Step 3 — Keep your branch up to date

If `main` has new commits while you are working, update your branch:

```bash
git fetch origin
git rebase origin/main
```

If there are conflicts, Git will pause and tell you which files to fix.
After fixing each file, run:

```bash
git add <file>
git rebase --continue
```

To cancel a rebase that went wrong:

```bash
git rebase --abort
```

---

### Step 4 — Open a Pull Request (PR) into `main`

When your work is ready:

```bash
git push origin feature/<your-branch-name>
```

Then go to the repository on GitHub and click **"Compare & pull request"**.
Set the **base branch** to `main` and describe what you changed.

---

### Step 5 — Undo changes safely

#### You have NOT pushed the commit yet (local only)

Keep your file changes but remove the last commit:

```bash
git reset --mixed HEAD~1
```

Throw away the last commit **and** the file changes (use with care):

```bash
git reset --hard HEAD~1
```

#### You HAVE already pushed (shared history — safe method)

Create a new commit that reverses a previous one. This does **not** rewrite history:

```bash
git revert <commit-hash>
# Example:
git revert a1b2c3d
```

> **Rule of thumb:** Use `git revert` on shared/pushed branches. Use `git reset` only on your own local commits.

---

### Step 6 — Save work temporarily with `git stash`

If you need to switch tasks before your current work is ready to commit:

```bash
# Save your current changes
git stash push -m "wip: description of what you were doing"

# Switch to another branch and do other work
git switch main

# Come back and restore your saved changes
git switch feature/<your-branch-name>
git stash pop
```

To see all saved stashes:

```bash
git stash list
```

---

### Step 7 — Copy a specific commit with `git cherry-pick`

If a fix lives on another branch and you only want that one commit (not the whole branch):

```bash
# Find the commit hash you want
git log --oneline feature/other-branch

# Apply it to your current branch
git cherry-pick <commit-hash>
# Example:
git cherry-pick a1b2c3d
```

If there is a conflict, resolve it, then run:

```bash
git add <file>
git cherry-pick --continue
```

To cancel:

```bash
git cherry-pick --abort
```

> **Team tip:** Tell your teammates when you cherry-pick a commit so they are not surprised by duplicate changes appearing in different branches.

---

### Quick Reference

| Goal | Command |
|---|---|
| Get latest `main` | `git pull origin main` |
| Create a branch | `git switch -c feature/<name>` |
| Update branch from `main` | `git fetch origin && git rebase origin/main` |
| Save work-in-progress | `git stash push -m "wip: <description>"` |
| Restore saved work | `git stash pop` |
| Undo local commit (keep files) | `git reset --mixed HEAD~1` |
| Undo a pushed commit (safe) | `git revert <commit-hash>` |
| Copy one commit to this branch | `git cherry-pick <commit-hash>` |
