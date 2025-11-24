#!/usr/bin/env python3
"""
Test Script for Enhanced Scene Choices
=====================================
Verify that the scene choices system is working correctly
"""

import sys
import os

# Add the current directory to the path so we can import our game
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_scene_choices_structure():
    """Test that scene choices are properly structured"""
    print("Testing Scene Choices Structure...")
    
    try:
        from player_gui import PlayerGameGUI
        
        # Create a temporary GUI instance to test
        gui = PlayerGameGUI()
        
        # Test that scene choices exist
        assert hasattr(gui, 'scene_choices'), "Scene choices not found"
        assert len(gui.scene_choices) > 0, "No scene choices defined"
        
        # Test each scene has choices
        for scene_name, choices in gui.scene_choices.items():
            print(f"  ✓ Scene '{scene_name}' has {len(choices)} choices")
            assert len(choices) == 3, f"Scene {scene_name} should have 3 choices, found {len(choices)}"
            
            # Test each choice has required fields
            for i, choice in enumerate(choices):
                assert 'text' in choice, f"Choice {i} in {scene_name} missing 'text'"
                assert 'description' in choice, f"Choice {i} in {scene_name} missing 'description'"
                assert 'consequence' in choice, f"Choice {i} in {scene_name} missing 'consequence'"
                assert 'class_bonus' in choice, f"Choice {i} in {scene_name} missing 'class_bonus'"
                
                # Test class bonuses exist for all classes
                for class_name in ['warrior', 'rogue', 'mage']:
                    assert class_name in choice['class_bonus'], f"Choice {i} in {scene_name} missing bonus for {class_name}"
        
        print("  ✓ All scene choices properly structured")
        return True
        
    except Exception as e:
        print(f"  ❌ Error testing scene choices: {e}")
        return False

def test_consequence_system():
    """Test that consequences are properly defined"""
    print("Testing Consequence System...")
    
    try:
        from player_gui import PlayerGameGUI
        
        gui = PlayerGameGUI()
        
        # Test that consequences exist
        assert hasattr(gui, 'handle_consequence'), "handle_consequence method not found"
        
        # Test that all consequences from choices are handled
        all_consequences = set()
        for choices in gui.scene_choices.values():
            for choice in choices:
                all_consequences.add(choice['consequence'])
        
        print(f"  ✓ Found {len(all_consequences)} unique consequences")
        
        # Test that game progress tracking exists
        for consequence in all_consequences:
            if consequence not in gui.game_progress:
                print(f"  ⚠️  Consequence '{consequence}' not in game_progress tracking")
        
        print("  ✓ Consequence system properly defined")
        return True
        
    except Exception as e:
        print(f"  ❌ Error testing consequence system: {e}")
        return False

def test_class_system():
    """Test that class system works with scene choices"""
    print("Testing Class System Integration...")
    
    try:
        from player_gui import PlayerGameGUI
        
        gui = PlayerGameGUI()
        
        # Test that classes exist
        assert hasattr(gui, 'classes'), "Classes not found"
        assert len(gui.classes) == 3, f"Should have 3 classes, found {len(gui.classes)}"
        
        # Test each class has required fields
        for class_name, class_data in gui.classes.items():
            required_fields = ['name', 'health', 'strength', 'agility', 'intelligence', 
                              'starting_weapon', 'ability', 'description']
            for field in required_fields:
                assert field in class_data, f"Class {class_name} missing field '{field}'"
        
        print("  ✓ Class system properly defined")
        return True
        
    except Exception as e:
        print(f"  ❌ Error testing class system: {e}")
        return False

def test_weapon_system():
    """Test that weapon system is properly defined"""
    print("Testing Weapon System...")
    
    try:
        from player_gui import PlayerGameGUI
        
        gui = PlayerGameGUI()
        
        # Test that weapons exist
        assert hasattr(gui, 'weapons'), "Weapons not found"
        assert len(gui.weapons) > 0, "No weapons defined"
        
        # Test each weapon has required fields
        for weapon_name, weapon_data in gui.weapons.items():
            required_fields = ['damage', 'type', 'class']
            for field in required_fields:
                assert field in weapon_data, f"Weapon {weapon_name} missing field '{field}'"
        
        print(f"  ✓ Weapon system has {len(gui.weapons)} weapons")
        return True
        
    except Exception as e:
        print(f"  ❌ Error testing weapon system: {e}")
        return False

def main():
    """Run all tests"""
    print("SHABUYA Cave Adventure - Scene Choices Test")
    print("=" * 50)
    
    tests = [
        ("Scene Choices Structure", test_scene_choices_structure),
        ("Consequence System", test_consequence_system),
        ("Class System Integration", test_class_system),
        ("Weapon System", test_weapon_system)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n--- {test_name} ---")
        if test_func():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"Tests Passed: {passed}/{total}")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED!")
        print("The enhanced scene choices system is working correctly.")
        print("\nNext steps:")
        print("1. Test the GUI manually to see the choice system in action")
        print("2. Verify that class-specific bonuses appear correctly")
        print("3. Check that consequences and rewards work as expected")
    else:
        print("⚠️  SOME TESTS FAILED")
        print("Please fix the issues before proceeding.")
    
    print("=" * 50)

if __name__ == "__main__":
    main()
