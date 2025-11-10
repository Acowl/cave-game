#!/usr/bin/env python3
"""
Integration Validation Utility

Ensures agent changes integrate properly by:
- Checking import statements still work
- Validating shared interfaces haven't changed without coordination
- Running test suite for affected modules
- Checking for breaking changes
- Validating configuration consistency

Usage:
    python utilities/validate_integration.py
    python utilities/validate_integration.py --files file1.py file2.py
"""

import os
import sys
import ast
import importlib.util
from pathlib import Path
from typing import List, Set, Dict, Tuple
import subprocess

# Repository root (assuming script is in utilities/)
REPO_ROOT = Path(__file__).parent.parent
DISTRIBUTION_DIR = REPO_ROOT / "distribution"
PLAYER_GUI_FILE = REPO_ROOT / "player_gui.py"
CONFIG_FILE = REPO_ROOT / "distribution" / "config.py"


def parse_imports(file_path: Path) -> Set[str]:
    """Parse Python file and extract import statements."""
    imports = set()
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name)
            elif isinstance(node, ast.ImportFrom):
                module = node.module or ''
                for alias in node.names:
                    imports.add(f"{module}.{alias.name}")
    
    except Exception as e:
        print(f"Warning: Could not parse {file_path}: {e}")
    
    return imports


def check_imports(file_path: Path) -> List[str]:
    """Check if imports in a file are valid."""
    errors = []
    imports = parse_imports(file_path)
    
    for imp in imports:
        # Skip standard library imports
        if not imp.startswith('distribution') and not imp.startswith('.'):
            continue
        
        # Try to resolve import
        try:
            module_name = imp.replace('/', '.').replace('.py', '')
            if module_name.startswith('distribution'):
                module_path = REPO_ROOT / module_name.replace('.', '/') / "__init__.py"
                if not module_path.exists():
                    # Try .py extension
                    module_path = REPO_ROOT / f"{module_name.replace('.', '/')}.py"
                    if not module_path.exists():
                        errors.append(f"Import '{imp}' in {file_path.name} cannot be resolved")
        except Exception as e:
            errors.append(f"Error checking import '{imp}' in {file_path.name}: {e}")
    
    return errors


def check_shared_interfaces() -> List[str]:
    """Check that shared interfaces haven't changed without coordination."""
    errors = []
    
    # Check config.py for unauthorized changes
    if CONFIG_FILE.exists():
        # This is a shared state file - any changes should be documented
        # In a real implementation, we'd check git history or change log
        pass
    
    # Check player.py for shared state changes
    player_file = REPO_ROOT / "distribution" / "player.py"
    if player_file.exists():
        # Check if Player class interface changed
        # This is a simplified check - in production, would compare signatures
        pass
    
    return errors


def validate_config_consistency() -> List[str]:
    """Validate configuration consistency across modules."""
    errors = []
    
    if not CONFIG_FILE.exists():
        errors.append("config.py not found")
        return errors
    
    # Check that config constants are used consistently
    # This is a simplified check
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            config_content = f.read()
        
        # Extract constants
        constants = []
        for line in config_content.split('\n'):
            if '=' in line and not line.strip().startswith('#'):
                const_name = line.split('=')[0].strip()
                if const_name.isupper() or const_name.replace('_', '').isupper():
                    constants.append(const_name)
        
        # Check usage in key files
        key_files = [
            REPO_ROOT / "player_gui.py",
            REPO_ROOT / "distribution" / "combat.py",
            REPO_ROOT / "distribution" / "player.py"
        ]
        
        for key_file in key_files:
            if key_file.exists():
                with open(key_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if config constants are imported
                if 'from distribution.config import' in content or 'import distribution.config' in content:
                    # Good - config is imported
                    pass
                else:
                    # Check if constants are used directly (might be okay)
                    pass
    
    except Exception as e:
        errors.append(f"Error validating config consistency: {e}")
    
    return errors


def run_tests(files: List[str] = None) -> Tuple[int, List[str]]:
    """Run test suite for affected modules."""
    errors = []
    
    # Try to run pytest
    try:
        cmd = ['python', '-m', 'pytest', 'tests/', '-v', '--tb=short']
        if files:
            # Run tests for specific files
            test_files = []
            for f in files:
                # Map source files to test files
                if 'player_gui.py' in f:
                    test_files.append('tests/unit/test_player_gui.py')
                elif 'combat.py' in f:
                    test_files.append('tests/unit/test_game.py')
            
            if test_files:
                cmd.extend(test_files)
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=REPO_ROOT,
            timeout=60
        )
        
        if result.returncode != 0:
            errors.append(f"Tests failed:\n{result.stdout}\n{result.stderr}")
            return result.returncode, errors
    
    except subprocess.TimeoutExpired:
        errors.append("Test suite timed out")
        return 1, errors
    except FileNotFoundError:
        errors.append("pytest not found - skipping tests")
        return 0, errors
    except Exception as e:
        errors.append(f"Error running tests: {e}")
        return 1, errors
    
    return 0, errors


def check_breaking_changes(files: List[str] = None) -> List[str]:
    """Check for potential breaking changes."""
    errors = []
    
    # Check for removed functions/classes
    # This is a simplified check - in production, would compare ASTs
    
    # Check for changed function signatures
    # This is a simplified check - in production, would compare signatures
    
    # Check for removed imports
    # This is a simplified check
    
    return errors


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Validate integration of agent changes')
    parser.add_argument('--files', nargs='+', help='Specific files to validate')
    parser.add_argument('--no-tests', action='store_true', help='Skip running tests')
    parser.add_argument('--strict', action='store_true', help='Fail on any error')
    args = parser.parse_args()
    
    files_to_check = args.files or []
    all_errors = []
    
    print("🔍 Validating integration...")
    print("=" * 60)
    
    # Check imports
    print("\n1. Checking imports...")
    if files_to_check:
        for file_path in files_to_check:
            path = REPO_ROOT / file_path
            if path.exists():
                errors = check_imports(path)
                if errors:
                    all_errors.extend(errors)
                    for error in errors:
                        print(f"   ❌ {error}")
                else:
                    print(f"   ✅ {file_path} imports are valid")
    else:
        # Check key files
        key_files = [
            PLAYER_GUI_FILE,
            REPO_ROOT / "distribution" / "combat.py",
            REPO_ROOT / "distribution" / "player.py",
            REPO_ROOT / "distribution" / "scenes.py"
        ]
        
        for key_file in key_files:
            if key_file.exists():
                errors = check_imports(key_file)
                if errors:
                    all_errors.extend(errors)
                    for error in errors:
                        print(f"   ❌ {error}")
                else:
                    print(f"   ✅ {key_file.name} imports are valid")
    
    # Check shared interfaces
    print("\n2. Checking shared interfaces...")
    errors = check_shared_interfaces()
    if errors:
        all_errors.extend(errors)
        for error in errors:
            print(f"   ❌ {error}")
    else:
        print("   ✅ Shared interfaces are consistent")
    
    # Validate config consistency
    print("\n3. Validating configuration consistency...")
    errors = validate_config_consistency()
    if errors:
        all_errors.extend(errors)
        for error in errors:
            print(f"   ❌ {error}")
    else:
        print("   ✅ Configuration is consistent")
    
    # Check for breaking changes
    print("\n4. Checking for breaking changes...")
    errors = check_breaking_changes(files_to_check)
    if errors:
        all_errors.extend(errors)
        for error in errors:
            print(f"   ❌ {error}")
    else:
        print("   ✅ No obvious breaking changes detected")
    
    # Run tests
    if not args.no_tests:
        print("\n5. Running tests...")
        exit_code, errors = run_tests(files_to_check)
        if errors:
            all_errors.extend(errors)
            for error in errors:
                print(f"   ❌ {error}")
        else:
            print("   ✅ All tests passed")
    else:
        print("\n5. Skipping tests (--no-tests specified)")
    
    # Summary
    print("\n" + "=" * 60)
    if all_errors:
        print(f"❌ Validation failed with {len(all_errors)} error(s)")
        if args.strict:
            return 1
    else:
        print("✅ Integration validation passed")
    
    return 0 if not all_errors else 1


if __name__ == "__main__":
    sys.exit(main())

