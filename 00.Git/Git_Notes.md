# Git & GitHub Cheat Sheet

A concise, navigable reference for everyday Git tasks, formatted in Markdown.

---

## 1. Configuration  
Set your identity once, then verify:

```bash
# Tell Git who you are
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# List all config settings
git config --list
```

---

## 2. Starting a Repository  

### A. Clone an existing repo  
```bash
git clone <SSH-or-HTTPS-URL>
cd <repo-folder>
```

### B. Initialize a new repo locally  
```bash
git init
```

---

## 3. Remotes  
```bash
# Add an “origin” remote for an existing local repo
git remote add origin <SSH-or-HTTPS-URL>

# List configured remotes
git remote -v

# Rename the remote (e.g. from “origin” to “upstream”)
git remote rename origin upstream
```

---

## 4. Checking Status & History  
```bash
git status       # What’s staged, unstaged, untracked?
git log          # Full commit history
git log --oneline --graph --decorate  # Compact, visual history
```

---

## 5. Staging & Committing  
```bash
git add <file>       # Stage a specific file
git add .            # Stage all changes in current directory
git commit -m "Msg"  # Commit staged changes with message
```

---

## 6. Pushing & Pulling  
```bash
# First push: set the upstream (remote + branch) at the same time
git push -u origin main  

# Subsequent pushes (working on the same branch):
git push           # thanks to -u, you don’t need origin/branch

# Fetch & merge changes from remote
git pull origin main

# Resync your local to remote
git pull --rebase origin main
```

---

## 7. Branching & Checkout  
```bash
git branch               # List all local branches
git branch -M newName    # Rename current branch to newName
git checkout <branch>    # Switch to existing branch
git checkout -b <branch> # Create + switch to new branch
git branch -d <branch>   # Delete a local branch (if merged)
```

---

## 8. Merging & Diff  
```bash
# View diff between your current HEAD and another branch
git diff <branch>

# Merge another branch into your current one
git merge <branch>
```

---

## 9. Undoing & Resetting  
> **⚠️ Warning:** Some of these commands rewrite history — use with care!

```bash
# Unstage changes in a file (keeps edits in working directory)
git reset <file>

# Unstage everything
git reset

# Reset to one commit back (moves HEAD to parent)
git reset --mixed HEAD~1     # default; doesn’t touch working files
git reset --soft  HEAD~1     # keeps staged changes
git reset --hard  HEAD~1     # discards changes in working directory

# Reset to a specific commit (by its hash)
git reset --hard <commit-hash>
```

---

## 10. Quick Tips  

- **Amend last commit** (to adjust message or include new staged changes):  
  ```bash
  git commit --amend
  ```
- **Stash unfinished work**:  
  ```bash
  git stash      # Save local changes
  git stash pop  # Reapply stashed changes
  ```
- **Restore a file from the last commit**:  
  ```bash
  git restore <file>
  ```
