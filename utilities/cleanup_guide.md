# Quick Cleanup Utility

Removes Python cache files and temporary build artifacts from the repository.

## Windows (PowerShell)

```powershell
# Remove all __pycache__ directories
Get-ChildItem -Path . -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force

# Remove all .pyc files
Get-ChildItem -Path . -Recurse -Filter "*.pyc" | Remove-Item -Force

# Remove pytest cache
if (Test-Path ".pytest_cache") { Remove-Item -Recurse -Force ".pytest_cache" }

Write-Host "Cleanup complete!" -ForegroundColor Green
```

## Linux/Mac (Bash)

```bash
#!/bin/bash

# Remove all __pycache__ directories
find . -type d -name "__pycache__" -exec rm -rf {} +

# Remove all .pyc files
find . -type f -name "*.pyc" -delete

# Remove pytest cache
rm -rf .pytest_cache

echo "Cleanup complete!"
```

## Usage

### Windows
```powershell
# Run directly
.\utilities\cleanup.ps1

# Or copy-paste the commands above
```

### Linux/Mac
```bash
# Make executable
chmod +x utilities/cleanup.sh

# Run
./utilities/cleanup.sh
```

## What Gets Removed

- `__pycache__/` directories (Python bytecode cache)
- `*.pyc` files (Compiled Python files)
- `.pytest_cache/` (Pytest cache)

## When to Run

- Before committing changes
- Before creating distribution builds
- When switching between Python versions
- After running tests

## Note

The `.gitignore` file is configured to ignore these files automatically, so they won't be committed to the repository. This utility is for local cleanup only.

