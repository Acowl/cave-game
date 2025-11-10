#!/usr/bin/env pwsh
# Quick cleanup script for Windows
# Removes Python cache files and temporary build artifacts

Write-Host "Starting cleanup..." -ForegroundColor Cyan

# Remove all __pycache__ directories
Write-Host "Removing __pycache__ directories..." -ForegroundColor Yellow
Get-ChildItem -Path . -Recurse -Directory -Filter "__pycache__" -ErrorAction SilentlyContinue | Remove-Item -Recurse -Force

# Remove all .pyc files
Write-Host "Removing .pyc files..." -ForegroundColor Yellow
Get-ChildItem -Path . -Recurse -Filter "*.pyc" -ErrorAction SilentlyContinue | Remove-Item -Force

# Remove pytest cache
Write-Host "Removing pytest cache..." -ForegroundColor Yellow
if (Test-Path ".pytest_cache") { Remove-Item -Recurse -Force ".pytest_cache" }

Write-Host "Cleanup complete!" -ForegroundColor Green

