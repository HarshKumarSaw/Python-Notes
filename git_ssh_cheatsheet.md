# Git & GitHub via SSH – Cheat Sheet

A complete reference for using Git and GitHub **securely via SSH** from the terminal (e.g., Termux).

---

## 1. Initial Configuration

```bash
# Set your identity
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# Check your configuration
git config --list
```

---

## 2. Generate & Add SSH Key to GitHub

```bash
# Generate a new SSH key
ssh-keygen -t ed25519 -C "you@example.com"

# Start the ssh-agent in the background
eval "$(ssh-agent -s)"

# Add your private key to the ssh-agent
ssh-add ~/.ssh/id_ed25519

# Show your public key
cat ~/.ssh/id_ed25519.pub
```

🔗 Go to [https://github.com/settings/ssh/new](https://github.com/settings/ssh/new) and paste the public key.

---

## 3. Test SSH Connection

```bash
ssh -T git@github.com
```

✅ You should see:
```
Hi username! You've successfully authenticated...
```

---

## 4. Clone Repository (SSH)

```bash
git clone git@github.com:username/repo-name.git
cd repo-name
```

---

## 5. Regular Git Commands (via SSH)

### A. Staging & Committing
```bash
git status              # Check changes
git add <file>          # Stage a file
git add .               # Stage all files
git commit -m "Message" # Commit staged changes
```

### B. Pushing & Pulling
```bash
git push -u origin main   # First push with upstream set
git push                  # Subsequent pushes
git pull origin main      # Pull latest changes from GitHub
```

---

## 6. Branching

```bash
git branch                # List branches
git checkout <branch>     # Switch branch
git checkout -b <branch>  # Create + switch
git branch -d <branch>    # Delete a local branch
git branch -M new-name    # Rename current branch
```

---

## 7. Remote Setup

```bash
# Set remote origin to use SSH
git remote add origin git@github.com:username/repo-name.git

# Verify the remote URL
git remote -v
```

---

## 8. Merging & Diff

```bash
git diff <branch>        # See difference from another branch
git merge <branch>       # Merge into current branch
```

---

## 9. Undoing & Resetting

```bash
git reset <file>              # Unstage a file
git reset                     # Unstage all files
git reset --mixed HEAD~1      # Reset last commit (keep changes)
git reset --hard HEAD~1       # Reset last commit (discard changes)
git reset --hard <commit-hash># Reset to specific commit
```

---

## 10. Tips & Helpers

```bash
git log                           # Commit history
git log --oneline --graph         # Compact visual history
git restore <file>               # Restore file to last commit
git stash                        # Save uncommitted changes
git stash pop                    # Reapply saved changes
git commit --amend               # Edit last commit
```

---

✅ Now you're set up to use Git and GitHub entirely via SSH!
