#!/usr/bin/env python3
"""
Test script for enhanced GUI system
"""
import sys
from pathlib import Path

def test_enhanced_gui():
    """Test enhanced GUI system imports and basic functionality"""
    print("🧪 Testing Enhanced GUI System...")
    
    # Test basic imports
    try:
        print("  📦 Testing tkinter import...")
        import tkinter as tk
        print("  ✅ tkinter: OK")
    except ImportError as e:
        print(f"  ❌ tkinter: {e}")
        print("  ⚠️ Tkinter not available in headless environment - normal in dev containers")
        return False
    
    try:
        print("  📦 Testing PIL import...")
        from PIL import Image, ImageTk
        print("  ✅ PIL: OK") 
    except ImportError as e:
        print(f"  ❌ PIL: {e}")
        return False
    
    try:
        print("  📦 Testing enhanced GUI import...")
        # Import without initializing GUI (headless safe)
        import enhanced_gui_system
        print("  ✅ Enhanced GUI module: OK")
    except ImportError as e:
        print(f"  ❌ Enhanced GUI: {e}")
        return False
    
    print("✅ Enhanced GUI system ready!")
    return True

def test_build_system():
    """Test build system integration"""
    print("\n🔧 Testing Build System Integration...")
    
    try:
        from build_config import BuildConfiguration
        from build_engine import UniversalBuilder
        
        config = BuildConfiguration()
        print(f"  📋 Available build targets: {len(config.list_targets())}")
        
        for target in config.list_targets()[:3]:  # Show first 3
            print(f"    • {target}")
        
        print("  ✅ Build system: OK")
        return True
        
    except ImportError as e:
        print(f"  ❌ Build system: {e}")
        return False

def test_steam_integration():
    """Test Steam integration"""
    print("\n🎮 Testing Steam Integration...")
    
    try:
        from steam_integration.steam_api import get_steam_integration
        steam = get_steam_integration()
        
        print(f"  🏆 Defined achievements: {len(steam.steam.achievements)}")
        
        # Show first few achievements
        for name, achievement in list(steam.steam.achievements.items())[:3]:
            print(f"    • {achievement.name}: {achievement.description}")
        
        print("  ✅ Steam integration: OK")
        return True
        
    except ImportError as e:
        print(f"  ❌ Steam integration: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 SHABUYA Cave Adventure - System Test")
    print("=" * 50)
    
    results = []
    
    # Run tests
    results.append(("Enhanced GUI", test_enhanced_gui()))
    results.append(("Build System", test_build_system()))
    results.append(("Steam Integration", test_steam_integration()))
    
    # Summary
    print("\n" + "=" * 50)
    print("📊 Test Results:")
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"  {status} {test_name}")
        if result:
            passed += 1
    
    print(f"\n🎯 Overall: {passed}/{len(results)} systems ready")
    
    if passed == len(results):
        print("🚀 ALL SYSTEMS GO - Ready to start Phase 1!")
    else:
        print("⚠️ Some systems need attention - see errors above")
    
    return passed == len(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
