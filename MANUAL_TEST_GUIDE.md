# 🧪 Manual Testing Guide - Enhanced Scene Choices

## 🎯 **Testing Objectives**

Verify that the enhanced scene choices system provides:
- ✅ Multiple interaction options per scene
- ✅ Class-specific bonuses and dialogue
- ✅ Meaningful consequences and rewards
- ✅ Proper progress tracking

---

## 🎮 **How to Test**

### **Step 1: Launch the Game**
```bash
python player_gui.py
```

### **Step 2: Select a Class**
- Choose **Warrior**, **Rogue**, or **Mage**
- Note the different starting stats and abilities

### **Step 3: Test Scene Choices**
For each scene, click the **"Interact"** button and verify:

#### **Cave Entrance**
- [ ] Choice window appears with 3 options
- [ ] Each choice shows detailed description
- [ ] Class-specific bonus text appears (green text)
- [ ] Selecting a choice shows consequence and reward
- [ ] Experience points are awarded

#### **Skull Chamber**
- [ ] 3 different choices available
- [ ] Class bonuses are appropriate for each class
- [ ] Consequences provide different rewards
- [ ] Progress is tracked in game state

#### **Primitive Village**
- [ ] Choices reflect different approaches to villagers
- [ ] Class-specific dialogue makes sense
- [ ] Rewards vary based on choice

#### **Chief's House**
- [ ] Options for different interaction styles
- [ ] Class bonuses enhance the chosen approach
- [ ] Consequences reflect the chosen action

#### **Healing Pool**
- [ ] Health restoration option works
- [ ] Magical insight options provide experience
- [ ] Class-specific benefits are clear

#### **Village Changed**
- [ ] Dark/combat-focused choices available
- [ ] Class-specific combat advantages shown
- [ ] High experience rewards for difficult choices

---

## ✅ **What to Verify**

### **Choice System**
- [ ] **3 choices per scene** (except healing pool which has special mechanics)
- [ ] **Choice window appears** when clicking "Interact"
- [ ] **Window is modal** (can't interact with main game until choice made)
- [ ] **Choices are clearly labeled** and described

### **Class-Specific Elements**
- [ ] **Warrior** gets tactical/combat bonuses
- [ ] **Rogue** gets stealth/perception bonuses  
- [ ] **Mage** gets magical/knowledge bonuses
- [ ] **Bonus text appears** in green italic text
- [ ] **Bonuses make sense** for each class

### **Consequences & Rewards**
- [ ] **Experience points awarded** (10-30 XP per choice)
- [ ] **Health restored** when choosing healing options
- [ ] **Story text updated** with consequence description
- [ ] **Progress tracked** in game state
- [ ] **Different rewards** for different choices

### **UI/UX**
- [ ] **Window styling** matches game theme
- [ ] **Text is readable** and well-formatted
- [ ] **Buttons are responsive** and clear
- [ ] **Window closes** after choice selection
- [ ] **Game state updates** immediately

---

## 🐛 **Common Issues to Check**

### **If Choices Don't Appear**
- Make sure you're clicking "Interact" not "Explore"
- Verify you're in a scene that has choices defined
- Check that the game is in "exploring" state

### **If Class Bonuses Don't Show**
- Verify you selected a class at game start
- Check that the class name matches exactly (warrior, rogue, mage)
- Ensure the choice has class_bonus defined

### **If Consequences Don't Work**
- Check that the consequence name matches in handle_consequence
- Verify that game_progress includes the consequence
- Ensure the effect function is properly defined

### **If UI Looks Wrong**
- Check that Tkinter is working properly
- Verify window geometry and styling
- Test on different screen resolutions

---

## 📊 **Expected Results**

### **Scene Choice Counts**
- Cave Entrance: 3 choices
- Skull Chamber: 3 choices  
- Primitive Village: 3 choices
- Chief's House: 3 choices
- Healing Pool: 3 choices
- Village Changed: 3 choices
- **Total: 18 unique choices**

### **Experience Rewards**
- Basic choices: 10-15 XP
- Moderate choices: 15-20 XP
- Advanced choices: 20-30 XP
- Health restoration: 50 HP + XP

### **Class Bonuses**
- **Warrior**: Combat, tactical, strength bonuses
- **Rogue**: Stealth, perception, agility bonuses
- **Mage**: Magic, knowledge, intelligence bonuses

---

## 🎉 **Success Criteria**

The enhanced scene choices system is working correctly if:

1. **✅ All 6 scenes show choice windows** when clicking "Interact"
2. **✅ Each scene has exactly 3 choices** with different approaches
3. **✅ Class-specific bonuses appear** and are appropriate
4. **✅ Consequences provide rewards** (XP, health, story progression)
5. **✅ Progress is tracked** and persists through the game
6. **✅ UI is responsive** and user-friendly
7. **✅ Story feels more engaging** with meaningful choices

---

## 🚀 **Next Steps After Testing**

If testing reveals the system works well:

1. **Weapon Discovery System** - Add weapon finding to scene choices
2. **Enhanced Combat** - Add enemy variety and weaknesses
3. **Inventory System** - Add item collection and management
4. **Save/Load System** - Add game persistence

If issues are found:

1. **Fix UI problems** - Window styling, responsiveness
2. **Balance rewards** - Adjust XP amounts, health restoration
3. **Improve class bonuses** - Make them more impactful
4. **Add missing features** - Fill in any gaps

---

*This manual testing ensures the enhanced scene choices provide the intended player experience before moving to the next feature.*
