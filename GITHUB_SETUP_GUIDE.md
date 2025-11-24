# GitHub Setup Guide

## ✅ Prerequisites Completed
- [x] `.gitignore` created
- [x] `README.md` created
- [x] DevSecOps pipeline configured
- [x] Docker image built and tested

## 🚀 Push to GitHub (Step-by-Step)

### Option 1: Using the Setup Script (Easiest)

1. **Run the setup script:**
   ```bash
   setup_github.bat
   ```

2. **Create GitHub repository:**
   - Go to https://github.com/new
   - Repository name: `shabuya-game`
   - Description: `RPG game with DevSecOps pipeline`
   - Choose Public or Private
   - **DO NOT** check "Initialize with README"
   - Click "Create repository"

3. **Connect and push:**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/shabuya-game.git
   git push -u origin main
   ```

### Option 2: Manual Setup

If the batch script doesn't work, run these commands manually:

```bash
# Initialize Git
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: DevSecOps pipeline with game foundation"

# Rename branch to main
git branch -M main

# Add remote (replace with your URL)
git remote add origin https://github.com/YOUR_USERNAME/shabuya-game.git

# Push to GitHub
git push -u origin main
```

## 🔍 Verify GitHub Actions

After pushing, the CI/CD pipeline will automatically run:

1. **Go to your repository on GitHub**
2. **Click the "Actions" tab**
3. **You should see a workflow running:**
   - ✅ Security scanning (Bandit, Safety)
   - ✅ Code formatting (Black)
   - ✅ Linting (Flake8)
   - ✅ Tests (Pytest)

## 📊 What Happens on Each Push

Every time you push code to GitHub:

1. **Build Stage**: GitHub Actions spins up Ubuntu container
2. **Install Stage**: Installs Python 3.10 and dependencies
3. **Security Stage**: 
   - Scans for vulnerable dependencies
   - Checks code for security issues
4. **Quality Stage**:
   - Checks code formatting
   - Runs linting
5. **Test Stage**: Runs your test suite

## 🛡️ Pipeline Status Badge

After your first successful run, add this to your README.md:

```markdown
![CI/CD Pipeline](https://github.com/YOUR_USERNAME/shabuya-game/actions/workflows/ci.yml/badge.svg)
```

## 🐛 Troubleshooting

### "fatal: not a git repository"
- Run: `git init`

### "Author identity unknown"
- Configure git:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  ```

### "Permission denied (publickey)"
- Set up SSH keys: https://docs.github.com/en/authentication/connecting-to-github-with-ssh
- Or use HTTPS URLs instead

### GitHub Actions failing
- Check the Actions tab for detailed logs
- Most common issues:
  - Syntax errors in Python files
  - Missing dependencies
  - Test failures

## 🎯 Next Steps After Push

1. **Verify pipeline passes** (green checkmarks in Actions tab)
2. **Set up branch protection** (Settings → Branches)
   - Require status checks before merging
   - Require pull request reviews
3. **Enable Dependabot** (Security → Dependabot)
   - Automated dependency updates
   - Security alerts
4. **Start Phase 2**: Begin Pygame development with confidence!

## 📝 Git Workflow Going Forward

```bash
# Make changes to your code
git add .
git commit -m "Descriptive message about what changed"
git push

# Pipeline runs automatically
# Check Actions tab for results
```

## 🔗 Useful Links

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Bandit Documentation](https://bandit.readthedocs.io/)
- [Black Documentation](https://black.readthedocs.io/)
- [Docker Hub](https://hub.docker.com/)

