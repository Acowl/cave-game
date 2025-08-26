#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Distribution Management
Central management for all distribution channels and deployment
"""

import json
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Any, Union
from dataclasses import dataclass, asdict, field
from datetime import datetime
import subprocess

from build_config import BuildConfiguration, get_build_config
from build_engine import UniversalBuilder

@dataclass 
class DeploymentTarget:
    """Configuration for a deployment target"""
    name: str
    platform: str
    active: bool = True
    
    # Connection details
    endpoint: Optional[str] = None
    credentials_file: Optional[str] = None
    
    # Build configuration
    build_target: str = "professional"
    auto_build: bool = True
    
    # Validation settings
    test_before_deploy: bool = True
    backup_before_deploy: bool = True

@dataclass
class ReleaseManifest:
    """Release manifest for tracking deployments"""
    version: str
    build_date: str
    build_number: int
    
    # Build info
    targets_built: Dict[str, str]  # target_name -> build_path
    file_hashes: Dict[str, str]    # file_path -> hash
    
    # Deployment info
    deployed_to: Dict[str, str]    # platform -> deployment_id
    deployment_date: Optional[str] = None
    
    # Release notes
    release_notes: str = ""
    breaking_changes: List[str] = field(default_factory=list)
    new_features: List[str] = field(default_factory=list)
    bug_fixes: List[str] = field(default_factory=list)

class DistributionManager:
    """Central distribution and deployment manager"""
    
    def __init__(self, project_root: Optional[Path] = None):
        self.project_root = project_root or Path(__file__).parent
        self.config = get_build_config()
        self.builder = UniversalBuilder(self.project_root)
        
        # Distribution targets
        self.targets = self._setup_distribution_targets()
        
        # Release management
        self.releases_dir = self.project_root / "releases"
        self.releases_dir.mkdir(exist_ok=True)
        
    def _setup_distribution_targets(self) -> Dict[str, DeploymentTarget]:
        """Setup distribution targets configuration"""
        targets = {}
        
        # GitHub Releases
        targets["github"] = DeploymentTarget(
            name="GitHub Releases",
            platform="github",
            build_target="professional",
            test_before_deploy=True
        )
        
        # Itch.io
        targets["itch"] = DeploymentTarget(
            name="Itch.io",
            platform="itch",
            build_target="itch",
            auto_build=True,
            active=False  # Not configured yet
        )
        
        # Steam (preparation only)
        targets["steam_prep"] = DeploymentTarget(
            name="Steam Preparation",
            platform="steam",
            build_target="steam_prep",
            auto_build=False,
            active=False  # Not ready yet
        )
        
        # Direct download (website)
        targets["direct"] = DeploymentTarget(
            name="Direct Download",
            platform="web",
            build_target="zip_basic",
            auto_build=True
        )
        
        return targets
    
    def create_release(self, version: Optional[str] = None, release_notes: str = "") -> ReleaseManifest:
        """Create a new release with all configured targets"""
        
        if version is None:
            version = self.config.metadata.version
        
        print(f"🚀 Creating release {version}...")
        
        # Create release directory
        release_date = datetime.now().strftime("%Y%m%d_%H%M%S")
        release_dir = self.releases_dir / f"v{version}_{release_date}"
        release_dir.mkdir(exist_ok=True)
        
        # Build all active targets
        targets_built = {}
        file_hashes = {}
        
        for target_name, deploy_config in self.targets.items():
            if not deploy_config.active or not deploy_config.auto_build:
                continue
                
            print(f"🏗️ Building {deploy_config.name}...")
            
            try:
                # Build the target
                build_result = self.builder.build_target(
                    deploy_config.build_target, 
                    clean=False
                )
                
                # Copy to release directory
                if build_result.is_file():
                    # ZIP file
                    dest_path = release_dir / build_result.name
                    shutil.copy2(build_result, dest_path)
                    targets_built[target_name] = str(dest_path)
                    
                    # Calculate hash
                    import hashlib
                    with open(dest_path, 'rb') as f:
                        file_hash = hashlib.sha256(f.read()).hexdigest()
                        file_hashes[build_result.name] = file_hash
                
                else:
                    # Directory
                    dest_path = release_dir / build_result.name
                    shutil.copytree(build_result, dest_path, dirs_exist_ok=True)
                    targets_built[target_name] = str(dest_path)
                
                print(f"  ✅ {deploy_config.name}: {dest_path}")
                
            except Exception as e:
                print(f"  ❌ {deploy_config.name}: {e}")
                continue
        
        # Create release manifest
        manifest = ReleaseManifest(
            version=version,
            build_date=datetime.now().isoformat(),
            build_number=self.config.metadata.build_number,
            targets_built=targets_built,
            file_hashes=file_hashes,
            deployed_to={},
            release_notes=release_notes
        )
        
        # Save manifest
        manifest_path = release_dir / "release_manifest.json"
        with open(manifest_path, 'w') as f:
            json.dump(asdict(manifest), f, indent=2)
        
        # Create release summary
        self._create_release_summary(release_dir, manifest)
        
        print(f"✅ Release {version} created: {release_dir}")
        return manifest
    
    def _create_release_summary(self, release_dir: Path, manifest: ReleaseManifest):
        """Create a human-readable release summary"""
        
        summary = f"""# 🗻 SHABUYA Cave Adventure - Release v{manifest.version}

**Build Date**: {manifest.build_date}
**Build Number**: {manifest.build_number}

## 📦 Available Downloads

"""
        
        for target_name, build_path in manifest.targets_built.items():
            target_config = self.targets.get(target_name)
            if target_config:
                file_path = Path(build_path)
                if file_path.is_file():
                    size_mb = file_path.stat().st_size / (1024 * 1024)
                    summary += f"- **{target_config.name}**: `{file_path.name}` ({size_mb:.1f} MB)\n"
                else:
                    summary += f"- **{target_config.name}**: `{file_path.name}` (Directory)\n"
        
        summary += f"""

## 🎮 Quick Start

### For Players:

1. **Download** the appropriate version for your platform
2. **Extract** the ZIP file to your desired location
3. **Run** the game launcher:
   - **Windows**: Double-click `LAUNCH_GAME.bat`
   - **Linux/macOS**: Run `./launch_game.sh` in terminal
   - **Any Platform**: Run `python launch_game.py`

### System Requirements:
- **Python 3.7+** (Download from https://python.org)
- **Operating System**: Windows 10+, Linux, or macOS 10.12+
- **Storage**: 50MB available space

## 📝 Release Notes

{manifest.release_notes}

## 🔒 File Integrity

"""
        
        for filename, file_hash in manifest.file_hashes.items():
            summary += f"- `{filename}`: `{file_hash[:16]}...`\n"
        
        summary += f"""

## 🚀 Deployment Status

"""
        
        if manifest.deployed_to:
            for platform, deployment_id in manifest.deployed_to.items():
                summary += f"- **{platform}**: {deployment_id}\n"
        else:
            summary += "- No deployments yet\n"
        
        summary += f"""

---

**Enjoy your adventure in the caves of Mount Shabuya!** 🗻⚔️

*Generated automatically by SHABUYA Distribution Manager*
"""
        
        with open(release_dir / "README.md", 'w') as f:
            f.write(summary)
    
    def deploy_to_github(self, manifest: ReleaseManifest) -> bool:
        """Deploy release to GitHub Releases"""
        print("🐙 Deploying to GitHub Releases...")
        
        # This would use GitHub API or gh CLI tool
        # For now, just prepare the files and instructions
        
        release_dir = Path(list(manifest.targets_built.values())[0]).parent
        
        instructions = f"""# 🚀 GitHub Release Deployment Instructions

## Automated Deployment (Recommended)

If you have the GitHub CLI (`gh`) installed:

```bash
cd {release_dir}

# Create release
gh release create v{manifest.version} \\
  --title "🗻 SHABUYA Cave Adventure v{manifest.version}" \\
  --notes-file README.md \\
  --generate-notes
  
# Upload assets
"""
        
        for build_path in manifest.targets_built.values():
            path = Path(build_path)
            if path.is_file():
                instructions += f"gh release upload v{manifest.version} {path.name}\n"
        
        instructions += f"""

## Manual Deployment

1. Go to your GitHub repository
2. Click "Releases" → "Create a new release"
3. Tag version: `v{manifest.version}`
4. Release title: `🗻 SHABUYA Cave Adventure v{manifest.version}`
5. Upload the following files:
"""
        
        for build_path in manifest.targets_built.values():
            path = Path(build_path)
            if path.is_file():
                instructions += f"   - {path.name}\n"
        
        instructions += f"""
6. Copy release notes from README.md
7. Publish release

## Release Notes Template

```markdown
{manifest.release_notes}

### Downloads
"""
        
        for target_name, build_path in manifest.targets_built.items():
            target_config = self.targets.get(target_name)
            path = Path(build_path)
            if target_config and path.is_file():
                size_mb = path.stat().st_size / (1024 * 1024)
                instructions += f"- **{target_config.name}**: {path.name} ({size_mb:.1f} MB)\n"
        
        instructions += "```"
        
        with open(release_dir / "github_deployment.md", 'w') as f:
            f.write(instructions)
        
        print(f"  ✅ GitHub deployment instructions created")
        return True
    
    def prepare_steam_build(self, manifest: ReleaseManifest) -> bool:
        """Prepare Steam build structure"""
        print("🎮 Preparing Steam build...")
        
        # Find Steam preparation build
        steam_build_path = None
        for target_name, build_path in manifest.targets_built.items():
            if target_name == "steam_prep":
                steam_build_path = Path(build_path)
                break
        
        if not steam_build_path:
            print("  ❌ Steam preparation build not found")
            return False
        
        # Create Steam build directory structure
        steam_dir = steam_build_path.parent / "steam_ready"
        steam_dir.mkdir(exist_ok=True)
        
        # Copy game files
        content_dir = steam_dir / "content"
        if content_dir.exists():
            shutil.rmtree(content_dir)
        shutil.copytree(steam_build_path, content_dir)
        
        # Create Steam build instructions
        instructions = f"""# 🎮 Steam Build Instructions

## Steam Partner Prerequisites

1. **Steam Partner Account**: Register at https://partner.steamgames.com
2. **Steamworks SDK**: Download from partner portal
3. **App ID**: Assigned by Steam after approval process

## Build Process

1. **Update App ID**: Set your assigned Steam App ID in `build_config.py`
2. **Configure Depots**: Update depot IDs in Steam configuration
3. **Test Build**: Use Steam SDK tools to test the build
4. **Upload to Steam**: Use ContentBuilder to upload

## Directory Structure

```
steam_ready/
├── content/              # Game content (this build)
├── steam_config/         # Steam VDF configuration files  
└── steamworks_sdk/       # Steam SDK (download separately)
```

## Steam Integration Checklist

### Basic Integration
- [ ] App ID configured
- [ ] Depot configuration updated
- [ ] Basic launcher tested with Steam
- [ ] Store page configured

### Advanced Integration (Optional)
- [ ] Steam achievements implemented
- [ ] Steam Cloud saves configured
- [ ] Steam overlay compatibility tested
- [ ] Steam statistics tracking

## Build Upload Commands

```bash
# Navigate to Steam SDK ContentBuilder
cd steamworks_sdk/tools/ContentBuilder

# Build and upload (replace with your actual IDs)
./builder_linux/steamcmd +login <username> +run_app_build ../../../steam_config/app_build.vdf +quit

# Windows equivalent
builder\\steamcmd.exe +login <username> +run_app_build ..\\..\\..\\steam_config\\app_build.vdf +quit
```

## Testing

1. **Local Testing**: Ensure game runs without Steam
2. **Steam Testing**: Test with Steam client in offline mode
3. **Achievement Testing**: Verify achievements work (if implemented)
4. **Store Testing**: Test store page preview

---

**Note**: This is a preparation build. Actual Steam deployment requires:
1. Approved Steam partner account
2. Completed store page
3. Content rating
4. Release date scheduling
"""
        
        with open(steam_dir / "STEAM_DEPLOYMENT.md", 'w') as f:
            f.write(instructions)
        
        print(f"  ✅ Steam build prepared: {steam_dir}")
        return True
    
    def list_releases(self) -> List[str]:
        """List all available releases"""
        releases = []
        if self.releases_dir.exists():
            for release_dir in self.releases_dir.iterdir():
                if release_dir.is_dir():
                    releases.append(release_dir.name)
        return sorted(releases, reverse=True)
    
    def get_latest_release(self) -> Optional[Path]:
        """Get the latest release directory"""
        releases = self.list_releases()
        if releases:
            return self.releases_dir / releases[0]
        return None

def main():
    """Distribution manager CLI"""
    import argparse
    
    parser = argparse.ArgumentParser(description="SHABUYA Distribution Manager")
    parser.add_argument("action", choices=["create", "list", "deploy"], help="Action to perform")
    parser.add_argument("--version", help="Release version")
    parser.add_argument("--notes", help="Release notes")
    parser.add_argument("--target", help="Deployment target")
    
    args = parser.parse_args()
    
    manager = DistributionManager()
    
    if args.action == "create":
        manifest = manager.create_release(args.version, args.notes or "")
        
        # Automatically prepare deployments
        manager.deploy_to_github(manifest)
        manager.prepare_steam_build(manifest)
        
    elif args.action == "list":
        releases = manager.list_releases()
        print("Available releases:")
        for release in releases:
            print(f"  • {release}")
            
    elif args.action == "deploy":
        print("Deployment functionality ready for implementation")

if __name__ == "__main__":
    main()
