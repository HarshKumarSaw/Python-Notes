# Git & GitHub SSH Setup Guide (Simplified)

A minimal, step-by-step guide for securely setting up Git with GitHub via SSH in Termux or any terminal.

---

## 1. Set Git Identity

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

---

## 2. Generate SSH Key

```bash
ssh-keygen -t ed25519 -C "you@example.com"
```

- Press **Enter** to accept default file location.
- Leave passphrase blank (optional).

---

## 3. Start SSH Agent and Add Key

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

---

## 4. Copy Public Key

```bash
cat ~/.ssh/id_ed25519.pub
```

📋 Copy the output.

---

## 5. Add SSH Key to GitHub

1. Visit: [https://github.com/settings/ssh/new](https://github.com/settings/ssh/new)
2. Paste your public key.
3. Name it (e.g. Termux SSH).
4. Click **Add SSH Key**.

---

## 6. Test SSH Connection

```bash
ssh -T git@github.com
```

✅ Expected:
```
Hi username! You've successfully authenticated...
```

---

## 7. Clone a Repo via SSH

```bash
git clone git@github.com:username/repo-name.git
```

📌 Done! You're now set up to use GitHub with SSH.
