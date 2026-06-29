# Ubuntu Linux Command Reference for Professional Web Developers

## Introduction
This guide contains the most commonly used Ubuntu/Linux commands for professional web development.
Each command includes:
- Purpose
- Syntax
- Example

---

# 1. Navigation

## pwd
Purpose: Show current directory.

Syntax:
```bash
pwd
```

Example:
```bash
pwd
```

## ls
Purpose: List files.

Syntax:
```bash
ls
ls -l
ls -la
```

Example:
```bash
ls -la
```

## cd

Syntax:
```bash
cd folder
cd ..
cd ~
cd /
```

Example:
```bash
cd ~/Desktop
```

---

# 2. File Management

## touch
```bash
touch app.py
```

## mkdir
```bash
mkdir project
mkdir -p app/templates
```

## cp
```bash
cp file.txt backup.txt
cp -r folder backup/
```

## mv
```bash
mv old.py new.py
```

## rm
```bash
rm file.txt
rm -rf folder
```

---

# 3. Search

## find
```bash
find . -name "*.py"
```

## grep
```bash
grep "Flask" app.py
grep -rn "login" .
```

---

# 4. Permissions

## chmod
```bash
chmod 755 script.sh
chmod +x run.sh
```

## chown
```bash
sudo chown user:user file.txt
```

---

# 5. Package Management

## apt

Update:
```bash
sudo apt update
```

Upgrade:
```bash
sudo apt upgrade
```

Install:
```bash
sudo apt install git
```

Remove:
```bash
sudo apt remove git
```

---

# 6. Git

Clone:
```bash
git clone URL
```

Status:
```bash
git status
```

Commit:
```bash
git add .
git commit -m "Initial commit"
```

Push:
```bash
git push origin main
```

---

# 7. Python

Version:
```bash
python3 --version
```

Virtual Environment:
```bash
python3 -m venv venv
source venv/bin/activate
deactivate
```

Install package:
```bash
pip install flask
```

---

# 8. Flask

Run:
```bash
flask run
```

Debug:
```bash
flask --debug run
```

---

# 9. Networking

```bash
ping google.com
curl https://example.com
wget URL
ssh user@server
scp file user@server:/path
```

---

# 10. Process Management

```bash
ps aux
top
kill PID
pkill python
```

---

# 11. Disk

```bash
df -h
du -sh .
lsblk
```

---

# 12. Archive

```bash
zip -r project.zip project/
unzip project.zip
tar -czf backup.tar.gz folder
tar -xzf backup.tar.gz
```

---

# 13. Environment Variables

```bash
echo $PATH
export APP_ENV=development
```

---

# 14. VS Code

```bash
code .
code file.py
```

---

# 15. Useful Shortcuts

```text
Ctrl + C   Stop process
Ctrl + D   Logout
Ctrl + R   Search history
Ctrl + L   Clear screen
Tab        Auto completion
history    Show command history
clear      Clear terminal
```

---

# Real Project Example

```bash
mkdir myproject
cd myproject
python3 -m venv venv
source venv/bin/activate
pip install flask
git init
code .
flask --debug run
```

This document is a concise professional reference. Advanced topics include sed, awk, xargs, systemctl, journalctl, cron, rsync, ssh keys, Docker, Nginx, tmux, bash scripting, systemd services, PostgreSQL, MySQL, and deployment workflows.
