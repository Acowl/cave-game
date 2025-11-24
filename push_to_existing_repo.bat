@echo off
REM Push to Existing GitHub Repository
REM Quick script to push your DevSecOps work to your existing repo

echo.
echo ========================================
echo   Push SHABUYA to Existing GitHub Repo
echo ========================================
echo.

REM Configure Git user (if needed)
echo [INFO] Checking Git configuration...
git config user.name >nul 2>&1
if errorlevel 1 (
    echo.
    echo Please enter your Git configuration:
    set /p GIT_NAME="Your Name: "
    set /p GIT_EMAIL="Your Email: "
    git config --global user.name "%GIT_NAME%"
    git config --global user.email "%GIT_EMAIL%"
    echo [OK] Git configured
)

echo.
echo [1/5] Initializing Git (if needed)...
git init
echo [OK] Git initialized

echo.
echo [2/5] Adding all files...
git add .
echo [OK] Files staged

echo.
echo [3/5] Creating commit...
git commit -m "Add DevSecOps pipeline: Docker, GitHub Actions, security scanning"
if errorlevel 1 (
    echo [WARNING] Commit might have failed (possibly no changes or already committed)
)
echo [OK] Commit created

echo.
echo [4/5] Setting branch to main...
git branch -M main
echo [OK] Branch set

echo.
echo [5/5] Connecting to your existing repository...
echo.
echo What is your GitHub repository URL?
echo (It should look like: https://github.com/USERNAME/REPO-NAME.git)
echo.
set /p REPO_URL="Repository URL: "

REM Check if remote already exists
git remote get-url origin >nul 2>&1
if not errorlevel 1 (
    echo [INFO] Updating existing remote...
    git remote set-url origin %REPO_URL%
) else (
    echo [INFO] Adding new remote...
    git remote add origin %REPO_URL%
)

echo.
echo ========================================
echo   Ready to Push!
echo ========================================
echo.
echo The following command will push your code:
echo   git push -u origin main
echo.
echo This will upload:
echo   - DevSecOps pipeline (Dockerfile, GitHub Actions)
echo   - Security scanning configuration
echo   - Your game code
echo   - Documentation
echo.
set /p CONFIRM="Push now? (Y/N): "
if /i "%CONFIRM%"=="Y" (
    echo.
    echo [PUSHING] Uploading to GitHub...
    git push -u origin main
    if errorlevel 1 (
        echo.
        echo [WARNING] Push failed. Common reasons:
        echo   - Authentication needed
        echo   - Branch conflicts
        echo   - Wrong URL
        echo.
        echo Try pushing manually:
        echo   git push -u origin main --force
        pause
        exit /b 1
    )
    echo.
    echo ========================================
    echo   SUCCESS! Code pushed to GitHub
    echo ========================================
    echo.
    echo Next: Check your repository's Actions tab to see the pipeline run!
    echo   URL: %REPO_URL:.git=%/actions
    echo.
) else (
    echo.
    echo Push cancelled. To push later, run:
    echo   git push -u origin main
    echo.
)

pause

