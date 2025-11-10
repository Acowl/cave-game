#!/bin/bash
# Quick cleanup script for Linux/Mac
# Removes Python cache files and temporary build artifacts

echo "Starting cleanup..."

# Remove all __pycache__ directories
echo "Removing __pycache__ directories..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null

# Remove all .pyc files
echo "Removing .pyc files..."
find . -type f -name "*.pyc" -delete 2>/dev/null

# Remove pytest cache
echo "Removing pytest cache..."
rm -rf .pytest_cache 2>/dev/null

echo "Cleanup complete!"

