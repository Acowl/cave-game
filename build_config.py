#!/usr/bin/env python3
"""
SHABUYA Cave Adventure - Universal Build Configuration
Scalable build system for multiple distribution channels
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
import json

@dataclass
class BuildTarget:
    """Configuration for a specific build target"""
    name: str
    description: str
    
    # File inclusion/exclusion
    include_patterns: List[str] = field(default_factory=list)
    exclude_patterns: List[str] = field(default_factory=list)
    
    # Platform specifics
    platforms: List[str] = field(default_factory=lambda: ["windows", "linux", "macos"])
    
    # Launchers to create
    launchers: Dict[str, bool] = field(default_factory=dict)
    
    # Packaging options
    create_zip: bool = True
    create_installer: bool = False
    
    # Steam/Store specific
    steam_ready: bool = False
    store_assets: bool = False
    
    # Version and branding
    version_suffix: str = ""
    
    def get_output_name(self, base_name: str, version: str) -> str:
        """Generate output package name"""
        suffix = f"-{self.version_suffix}" if self.version_suffix else ""
        return f"{base_name}-v{version}{suffix}"

@dataclass
class GameMetadata:
    """Game metadata for all distribution channels"""
    # Basic info
    name: str = "SHABUYA Cave Adventure"
    short_name: str = "SHABUYA"
    version: str = "1.0.0"
    build_number: int = 1
    
    # Descriptions
    tagline: str = "A Thrilling Text-Based RPG Adventure"
    description: str = "Explore mysterious caves, battle creatures, and uncover ancient secrets"
    long_description: str = ""
    
    # Technical
    python_min_version: Tuple[int, int] = (3, 7)
    engine: str = "Python"
    
    # Legal
    developer: str = "SHABUYA Development Team"
    publisher: str = "Indie Games Studio"
    copyright_year: int = 2024
    
    # Steam specific
    steam_app_id: Optional[int] = None
    steam_depot_ids: Dict[str, int] = field(default_factory=dict)
    
    # Store presence
    website: str = ""
    support_email: str = ""
    
    # Categories and tags
    genre_primary: str = "RPG"
    genres: List[str] = field(default_factory=lambda: ["RPG", "Adventure", "Indie"])
    tags: List[str] = field(default_factory=lambda: ["Story Rich", "Turn-Based", "Fantasy"])
    
    # Age rating
    age_rating: str = "Everyone 10+"
    content_warnings: List[str] = field(default_factory=lambda: ["Fantasy Violence"])

class BuildConfiguration:
    """Central build configuration manager"""
    
    def __init__(self, project_root: Optional[Path] = None):
        self.project_root = project_root or Path(__file__).parent
        self.metadata = GameMetadata()
        self.targets = self._define_build_targets()
        
    def _define_build_targets(self) -> Dict[str, BuildTarget]:
        """Define all supported build targets"""
        
        targets = {}
        
        # Basic ZIP distribution (current)
        targets["zip_basic"] = BuildTarget(
            name="Basic ZIP Distribution",
            description="Simple ZIP package for direct download",
            include_patterns=[
                "src/**/*.py",
                "scripts/*.py", 
                "scripts/*.bat",
                "scripts/*.sh",
                "README.md",
                "requirements.txt"
            ],
            exclude_patterns=[
                "__pycache__/**",
                "*.pyc",
                "tests/**",
                "tools/**"
            ],
            launchers={
                "python": True,
                "batch": True,
                "shell": True,
                "desktop": False
            },
            create_zip=True,
            version_suffix="Basic"
        )
        
        # Professional distribution 
        targets["professional"] = BuildTarget(
            name="Professional Distribution",
            description="Full-featured package with all launchers",
            include_patterns=[
                "src/**/*.py",
                "scripts/**",
                "docs/**",
                "README.md",
                "requirements.txt",
                "LICENSE.txt"
            ],
            exclude_patterns=[
                "__pycache__/**",
                "*.pyc",
                "tests/test_*.py",
                "tools/debug_*.py"
            ],
            launchers={
                "python": True,
                "batch": True, 
                "shell": True,
                "desktop": True,
                "gui_launcher": True
            },
            create_zip=True,
            create_installer=True,
            version_suffix="Professional"
        )
        
        # Steam preparation
        targets["steam_prep"] = BuildTarget(
            name="Steam Preparation Build",
            description="Steam-ready build with proper structure",
            include_patterns=[
                "src/**/*.py",
                "scripts/steam_launcher.py",
                "steam_assets/**",
                "game_assets/**",
                "README.md",
                "LICENSE.txt"
            ],
            exclude_patterns=[
                "__pycache__/**",
                "*.pyc",
                "tests/**",
                "tools/**",
                "docs/development/**"
            ],
            launchers={
                "steam": True,
                "python": True,
                "desktop": True,
                "native": True
            },
            create_zip=False,
            steam_ready=True,
            store_assets=True,
            version_suffix="Steam"
        )
        
        # Native executable builds  
        targets["native_builds"] = BuildTarget(
            name="Native Executable Builds",
            description="PyInstaller native builds for Steam",
            include_patterns=[
                "src/**/*.py",
                "game_assets/**",
                "steam_integration/**",
                "requirements.txt"
            ],
            exclude_patterns=[
                "__pycache__/**",
                "*.pyc",
                "tests/**",
                "distribution/**"
            ],
            platforms=["windows", "linux", "macos"],
            launchers={
                "native": True,
                "steam": True
            },
            create_zip=False,
            steam_ready=True,
            version_suffix="Native"
        )
        
        # Itch.io optimized
        targets["itch"] = BuildTarget(
            name="Itch.io Distribution",
            description="Optimized for itch.io platform",
            include_patterns=[
                "src/**/*.py",
                "scripts/*.py",
                "itch_assets/**",
                "README.md"
            ],
            exclude_patterns=[
                "__pycache__/**",
                "*.pyc",
                "tests/**",
                "steam_assets/**"
            ],
            launchers={
                "python": True,
                "batch": True,
                "shell": True,
                "itch_launcher": True
            },
            create_zip=True,
            version_suffix="Itch"
        )
        
        return targets
    
    def get_target(self, target_name: str) -> BuildTarget:
        """Get specific build target configuration"""
        if target_name not in self.targets:
            raise ValueError(f"Unknown build target: {target_name}")
        return self.targets[target_name]
    
    def list_targets(self) -> List[str]:
        """List all available build targets"""
        return list(self.targets.keys())
    
    def save_config(self, config_path: Optional[Path] = None):
        """Save configuration to JSON file"""
        if config_path is None:
            config_path = self.project_root / "build_config.json"
            
        config_data = {
            "metadata": {
                "name": self.metadata.name,
                "version": self.metadata.version,
                "build_number": self.metadata.build_number,
                "developer": self.metadata.developer,
                "publisher": self.metadata.publisher,
                # Add more fields as needed
            },
            "targets": {
                name: {
                    "name": target.name,
                    "description": target.description,
                    "include_patterns": target.include_patterns,
                    "exclude_patterns": target.exclude_patterns,
                    "platforms": target.platforms,
                    "launchers": target.launchers,
                    "create_zip": target.create_zip,
                    "steam_ready": target.steam_ready,
                    "version_suffix": target.version_suffix
                }
                for name, target in self.targets.items()
            }
        }
        
        with open(config_path, 'w') as f:
            json.dump(config_data, f, indent=2)
    
    def load_config(self, config_path: Optional[Path] = None):
        """Load configuration from JSON file"""
        if config_path is None:
            config_path = self.project_root / "build_config.json"
        
        if not config_path.exists():
            return
            
        with open(config_path, 'r') as f:
            config_data = json.load(f)
        
        # Load metadata
        if "metadata" in config_data:
            for key, value in config_data["metadata"].items():
                if hasattr(self.metadata, key):
                    setattr(self.metadata, key, value)

# Global configuration instance
build_config = BuildConfiguration()

def get_build_config() -> BuildConfiguration:
    """Get the global build configuration"""
    return build_config

# Steam-specific configuration
STEAM_CONFIG = {
    "app_build": {
        "appid": 0,  # Will be assigned by Steam
        "desc": "SHABUYA Cave Adventure Build",
        "buildoutput": "../steamworks_sdk/tools/ContentBuilder/output",
        "contentroot": "./steam_build",
        "setlive": "",
        "preview": 1,
        "local": ""
    },
    "depots": {
        "windows": {
            "depot_id": 0,  # Will be assigned by Steam
            "file_mapping": {
                "LocalPath": "*",
                "DepotPath": ".",
                "recursive": 1
            }
        },
        "linux": {
            "depot_id": 0,  # Will be assigned by Steam
            "file_mapping": {
                "LocalPath": "*", 
                "DepotPath": ".",
                "recursive": 1
            }
        },
        "macos": {
            "depot_id": 0,  # Will be assigned by Steam
            "file_mapping": {
                "LocalPath": "*",
                "DepotPath": ".",
                "recursive": 1
            }
        }
    }
}

if __name__ == "__main__":
    # Example usage and testing
    config = BuildConfiguration()
    
    print("Available build targets:")
    for target_name in config.list_targets():
        target = config.get_target(target_name)
        print(f"  • {target.name}: {target.description}")
    
    # Save example configuration
    config.save_config()
    print("\nConfiguration saved to build_config.json")
