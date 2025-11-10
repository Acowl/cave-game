#!/usr/bin/env python3
"""
Agent Conflict Detection Utility

Scans modified files against ACTIVE_TASKS.md to detect potential conflicts
between agents working on the same files.

Usage:
    python utilities/check_agent_conflicts.py
    python utilities/check_agent_conflicts.py --files file1.py file2.py
"""

import os
import re
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Set, Tuple

# Repository root (assuming script is in utilities/)
REPO_ROOT = Path(__file__).parent.parent
TASKS_FILE = REPO_ROOT / ".cursor" / "tasks" / "ACTIVE_TASKS.md"
AGENTS_DIR = REPO_ROOT / ".cursor" / "agents"


def parse_active_tasks() -> Dict[str, Dict]:
    """Parse ACTIVE_TASKS.md and extract file assignments."""
    if not TASKS_FILE.exists():
        return {}
    
    tasks = {}
    current_task = None
    
    with open(TASKS_FILE, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse task entries
    task_pattern = r'### Task ID: (TASK-\d+)'
    task_matches = list(re.finditer(task_pattern, content))
    
    for i, match in enumerate(task_matches):
        task_id = match.group(1)
        task_start = match.start()
        task_end = task_matches[i + 1].start() if i + 1 < len(task_matches) else len(content)
        task_content = content[task_start:task_end]
        
        # Extract agent
        agent_match = re.search(r'\*\*Assigned Agent\*\*: (.+)', task_content)
        agent = agent_match.group(1).strip() if agent_match else "unknown"
        
        # Extract status
        status_match = re.search(r'\*\*Status\*\*: (.+)', task_content)
        status = status_match.group(1).strip() if status_match else "unknown"
        
        # Extract files affected
        files_section = re.search(r'#### Files Affected\n(.*?)(?=\n####|\Z)', task_content, re.DOTALL)
        files = []
        if files_section:
            file_lines = files_section.group(1).strip().split('\n')
            for line in file_lines:
                if line.strip().startswith('-'):
                    # Extract file path from markdown list item
                    file_match = re.search(r'`([^`]+)`', line)
                    if file_match:
                        files.append(file_match.group(1))
        
        tasks[task_id] = {
            'agent': agent,
            'status': status,
            'files': files
        }
    
    return tasks


def get_modified_files(files: List[str] = None) -> Set[str]:
    """Get list of modified files (from git or provided list)."""
    if files:
        return set(files)
    
    # Try to get modified files from git
    try:
        import subprocess
        result = subprocess.run(
            ['git', 'diff', '--name-only', 'HEAD'],
            capture_output=True,
            text=True,
            cwd=REPO_ROOT
        )
        if result.returncode == 0:
            modified = set(result.stdout.strip().split('\n'))
            return {f for f in modified if f}
    except Exception:
        pass
    
    return set()


def check_conflicts(modified_files: Set[str], tasks: Dict[str, Dict]) -> List[Tuple[str, str, str]]:
    """Check for conflicts between modified files and active tasks."""
    conflicts = []
    
    for task_id, task_info in tasks.items():
        # Only check active tasks
        if task_info['status'] not in ['pending', 'in_progress']:
            continue
        
        task_files = set(task_info['files'])
        task_agent = task_info['agent']
        
        # Check for overlapping files
        overlapping = modified_files & task_files
        
        if overlapping:
            for file in overlapping:
                conflicts.append((file, task_id, task_agent))
    
    return conflicts


def check_agent_ownership(file_path: str) -> List[str]:
    """Check which agents own/modify a file based on agent role definitions."""
    owners = []
    
    if not AGENTS_DIR.exists():
        return owners
    
    # Check each agent role file
    for agent_file in AGENTS_DIR.glob("agent-*.md"):
        agent_name = agent_file.stem.replace("agent-", "")
        
        try:
            with open(agent_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check primary ownership
            primary_match = re.search(r'## Primary File Ownership.*?## Secondary', content, re.DOTALL)
            if primary_match:
                primary_section = primary_match.group(0)
                if file_path in primary_section:
                    owners.append(f"{agent_name} (primary)")
            
            # Check secondary permissions
            secondary_match = re.search(r'## Secondary.*?## Forbidden', content, re.DOTALL)
            if secondary_match:
                secondary_section = secondary_match.group(0)
                if file_path in secondary_section:
                    owners.append(f"{agent_name} (secondary)")
        
        except Exception:
            continue
    
    return owners


def main():
    parser = argparse.ArgumentParser(description='Check for agent conflicts')
    parser.add_argument('--files', nargs='+', help='Specific files to check')
    parser.add_argument('--strict', action='store_true', help='Fail on any conflict')
    args = parser.parse_args()
    
    # Parse tasks
    tasks = parse_active_tasks()
    
    if not tasks:
        print("No active tasks found. No conflicts detected.")
        return 0
    
    # Get modified files
    modified_files = get_modified_files(args.files)
    
    if not modified_files:
        print("No modified files to check.")
        return 0
    
    # Check for conflicts
    conflicts = check_conflicts(modified_files, tasks)
    
    if conflicts:
        print("⚠️  CONFLICTS DETECTED:")
        print("=" * 60)
        
        conflict_files = {}
        for file, task_id, agent in conflicts:
            if file not in conflict_files:
                conflict_files[file] = []
            conflict_files[file].append((task_id, agent))
        
        for file, task_info in conflict_files.items():
            print(f"\n📄 File: {file}")
            owners = check_agent_ownership(file)
            if owners:
                print(f"   Owners: {', '.join(owners)}")
            
            print("   Conflicts with active tasks:")
            for task_id, agent in task_info:
                print(f"   - {task_id} ({agent})")
            
            print("\n   Action required:")
            print("   - Check ACTIVE_TASKS.md for task details")
            print("   - Coordinate with conflicting agent")
            print("   - Update task status if needed")
        
        if args.strict:
            return 1
    else:
        print("✅ No conflicts detected.")
        print(f"   Checked {len(modified_files)} file(s) against {len(tasks)} active task(s)")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())

