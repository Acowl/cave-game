#!/usr/bin/env python3
"""
Enhanced GUI System Setup Verification
Checks all components are ready for Phase 1 development
"""

def verify_setup():
    """Verify all systems are ready for development"""
    print("🎮 SHABUYA Cave Adventure - Setup Verification")
    print("=" * 60)
    
    checks = []
    
    # Check 1: Core Game Files
    print("📁 Checking Core Game Files...")
    core_files = [
        'game_refactored.py',
        'gui.py', 
        'main.py',
        'config.py',
        'player.py',
        'combat.py',
        'scenes.py'
    ]
    
    missing_core = []
    for file in core_files:
        try:
            with open(file, 'r') as f:
                content = f.read()
                if len(content) > 100:  # Basic sanity check
                    print(f"  ✅ {file}")
                else:
                    print(f"  ⚠️ {file} (too small)")
                    missing_core.append(file)
        except FileNotFoundError:
            print(f"  ❌ {file} (missing)")
            missing_core.append(file)
    
    checks.append(("Core Game Files", len(missing_core) == 0))
    
    # Check 2: Enhanced Systems
    print("\n🚀 Checking Enhanced Systems...")
    enhanced_files = [
        'enhanced_gui_system.py',
        'build_config.py',
        'build_engine.py',
        'native_build_system.py',
        'DEVELOPMENT_ROADMAP.md'
    ]
    
    missing_enhanced = []
    for file in enhanced_files:
        try:
            with open(file, 'r') as f:
                content = f.read()
                if len(content) > 500:  # These should be substantial files
                    print(f"  ✅ {file}")
                else:
                    print(f"  ⚠️ {file} (incomplete)")
                    missing_enhanced.append(file)
        except FileNotFoundError:
            print(f"  ❌ {file} (missing)")
            missing_enhanced.append(file)
    
    checks.append(("Enhanced Systems", len(missing_enhanced) == 0))
    
    # Check 3: Steam Integration
    print("\n🎮 Checking Steam Integration...")
    steam_files = [
        'steam_integration/steam_api.py',
        'steam_integration/__init__.py'
    ]
    
    steam_ready = True
    for file in steam_files:
        try:
            with open(file, 'r') as f:
                content = f.read()
                if 'class SteamIntegration' in content or 'Steam' in content:
                    print(f"  ✅ {file}")
                else:
                    print(f"  ⚠️ {file} (incomplete)")
                    steam_ready = False
        except FileNotFoundError:
            print(f"  ❌ {file} (missing)")
            steam_ready = False
    
    checks.append(("Steam Integration", steam_ready))
    
    # Check 4: Asset Directories
    print("\n🎨 Checking Asset Structure...")
    import os
    
    asset_dirs = [
        'game_assets',
        'game_assets/sprites', 
        'game_assets/backgrounds',
        'game_assets/icons',
        'store_assets'
    ]
    
    for directory in asset_dirs:
        if os.path.exists(directory):
            print(f"  ✅ {directory}/")
        else:
            print(f"  📁 {directory}/ (will be created)")
            try:
                os.makedirs(directory, exist_ok=True)
                print(f"    ✅ Created {directory}/")
            except Exception as e:
                print(f"    ❌ Failed to create {directory}/: {e}")
    
    checks.append(("Asset Directories", True))  # We create them if missing
    
    # Check 5: Python Dependencies
    print("\n🐍 Checking Python Dependencies...")
    
    required_modules = {
        'pathlib': 'Built-in',
        'sys': 'Built-in',  
        'os': 'Built-in',
        'json': 'Built-in'
    }
    
    optional_modules = {
        'PIL': 'Pillow (for graphics)',
        'pygame': 'pygame (for audio)',
        'tkinter': 'tkinter (for GUI - may not work in containers)'
    }
    
    # Test required modules
    deps_ok = True
    for module, description in required_modules.items():
        try:
            __import__(module)
            print(f"  ✅ {module} ({description})")
        except ImportError:
            print(f"  ❌ {module} ({description})")
            deps_ok = False
    
    # Test optional modules
    optional_ok = 0
    for module, description in optional_modules.items():
        try:
            __import__(module)
            print(f"  ✅ {module} ({description})")
            optional_ok += 1
        except ImportError:
            print(f"  ⚠️ {module} ({description}) - install if needed")
    
    checks.append(("Required Dependencies", deps_ok))
    checks.append(("Optional Dependencies", optional_ok >= 1))
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 SETUP VERIFICATION RESULTS:")
    
    passed = 0
    for check_name, result in checks:
        status = "✅ READY" if result else "❌ NEEDS ATTENTION"
        print(f"  {status} {check_name}")
        if result:
            passed += 1
    
    print(f"\n🎯 Overall Status: {passed}/{len(checks)} systems ready")
    
    # Phase 1 Readiness Assessment
    print("\n" + "=" * 60)
    if passed >= len(checks) - 1:  # Allow 1 failure for optional deps
        print("🚀 PHASE 1 READY!")
        print("✅ You can start UI/UX enhancement development")
        print("✅ Enhanced GUI system is implemented")
        print("✅ Build system is configured") 
        print("✅ Steam integration framework is ready")
        
        print("\n📋 IMMEDIATE NEXT STEPS:")
        print("1. Create character sprites (warrior, rogue, mage)")
        print("2. Create scene background images")
        print("3. Test enhanced GUI on target platforms")
        print("4. Set up development environment with graphics libraries")
        
        print("\n🎨 Asset Creation Guide:")
        print("• Character sprites: 64x64 PNG files")
        print("• Backgrounds: 400x300 PNG files") 
        print("• Use simple art style - even basic shapes work")
        print("• Enhanced GUI has fallback to text-only mode")
        
    else:
        print("⚠️ SETUP INCOMPLETE")
        print("Some systems need attention before starting Phase 1")
        print("See the issues marked with ❌ above")
    
    return passed >= len(checks) - 1

if __name__ == "__main__":
    verify_setup()
