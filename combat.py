#!/usr/bin/env python3
"""
Cave Game Combat System Module

This module handles all combat-related functionality including:
- Weapon effectiveness calculations
- Combat damage resolution
- Weapon inventory management
- Battle mechanics and stat checking

The combat system supports class-based gameplay with weapon specialization.
"""

from config import STAT_REQUIREMENT, STARTING_STAT_VALUE, FINAL_BOSS_STAT_REQUIREMENT
from item import dagger, axe, wand, enhanced_dagger, enhanced_axe, enhanced_wand

def get_available_weapons(player):
    """Get list of weapons available to the player."""
    weapons = [player.weapon]  # Always include starting weapon
    
    # Add collected enhanced weapons
    if hasattr(player, 'collected_weapons'):
        for weapon in player.collected_weapons:
            if weapon not in weapons:
                weapons.append(weapon)
    
    return weapons

def check_weapon_effectiveness(player, chosen_weapon, enemy_type="normal"):
    """Check if weapon is effective against enemy type"""
    if enemy_type == "chief":
        # Enhanced weapons work if they match player's class
        if chosen_weapon in [enhanced_dagger, enhanced_axe, enhanced_wand]:
            player_class_weapon = None
            if player.weapon == dagger:
                player_class_weapon = enhanced_dagger
            elif player.weapon == axe:
                player_class_weapon = enhanced_axe
            elif player.weapon == wand:
                player_class_weapon = enhanced_wand
            
            return chosen_weapon == player_class_weapon
        
        # Default weapons work with high stats
        elif chosen_weapon == dagger and hasattr(player, 'agility') and player.agility >= STAT_REQUIREMENT:
            return True
        elif chosen_weapon == axe and hasattr(player, 'strength') and player.strength >= STAT_REQUIREMENT:
            return True
        elif chosen_weapon == wand and hasattr(player, 'intelligence') and player.intelligence >= STAT_REQUIREMENT:
            return True
    
    elif enemy_type == "divine_heart":
        # Final boss requires enhanced weapon and combat readiness
        enhanced_weapon_equipped = chosen_weapon in [enhanced_dagger, enhanced_axe, enhanced_wand]
        if not enhanced_weapon_equipped:
            return False
        
        # Calculate combat readiness
        main_stat = 0
        if chosen_weapon == enhanced_dagger:
            main_stat = getattr(player, 'agility', STARTING_STAT_VALUE)
        elif chosen_weapon == enhanced_axe:
            main_stat = getattr(player, 'strength', STARTING_STAT_VALUE)
        elif chosen_weapon == enhanced_wand:
            main_stat = getattr(player, 'intelligence', STARTING_STAT_VALUE)
        
        vitality = getattr(player, 'vitality', STARTING_STAT_VALUE)
        total_combat_readiness = main_stat + vitality - (STARTING_STAT_VALUE * 2)
        
        return total_combat_readiness >= FINAL_BOSS_STAT_REQUIREMENT
    
    return True  # Normal enemies

def execute_weapon_attack(player, chosen_weapon, enemy_type="normal"):
    """Execute weapon attack and return result"""
    if enemy_type == "alley_creature":
        return execute_alley_attack(chosen_weapon)
    elif enemy_type == "chief":
        return execute_chief_attack(player, chosen_weapon)
    elif enemy_type == "divine_heart":
        return execute_divine_heart_attack(player, chosen_weapon)
    
    return True, "Attack successful!"

def execute_alley_attack(chosen_weapon):
    """Execute attack against alley creature"""
    if chosen_weapon == dagger:
        message = ("You lunge forward with cat-like agility! "
                  "The creature swings its massive club, but you duck and weave beneath its guard. "
                  "Your blade finds the gaps in its thick hide, striking with surgical precision. "
                  "With a final, lightning-fast thrust, you drive your dagger deep into its heart.")
    elif chosen_weapon == axe:
        message = ("You raise your axe high and charge with a mighty war cry! "
                  "The creature's club crashes against your axe in a shower of sparks and splinters. "
                  "Your superior strength and weapon training quickly turn the tide. "
                  "With a devastating overhead swing, you cleave through the beast's defenses.")
    elif chosen_weapon == wand:
        message = ("You point your wand at the creature and channel your magical energy! "
                  "Bolts of mystical force streak through the air, striking the beast repeatedly. "
                  "The creature staggers as arcane energy burns through its primitive flesh. "
                  "A final, concentrated blast of magic brings the beast to its knees.")
    elif chosen_weapon in [enhanced_dagger, enhanced_axe, enhanced_wand]:
        if chosen_weapon == enhanced_dagger:
            message = ("The Shadow Blade erupts with dark energy as you strike! "
                      "Your enhanced dagger cuts through the creature's hide like butter. "
                      "Dark energy courses through each wound, weakening the beast rapidly. "
                      "With supernatural speed, you deliver a flurry of shadow-enhanced strikes.")
        elif chosen_weapon == enhanced_axe:
            message = ("The Bone Crusher resonates with primal power! "
                      "Your enhanced axe cleaves through the creature's club like paper. "
                      "Each swing carries devastating force that shakes the alley walls. "
                      "A final earth-shaking blow crushes the beast completely.")
        elif chosen_weapon == enhanced_wand:
            message = ("The Skull Scepter blazes with arcane might! "
                      "Torrents of magical energy pour from your enhanced wand. "
                      "The creature's primitive defenses crumble before your mystical assault. "
                      "A concentrated beam of pure magic overwhelms the beast utterly.")
    else:
        message = "Your weapon proves effective against the creature."
    
    return True, message

def execute_chief_attack(player, chosen_weapon):
    """Execute attack against the Chief"""
    effective = check_weapon_effectiveness(player, chosen_weapon, "chief")
    
    if effective:
        if chosen_weapon in [enhanced_dagger, enhanced_axe, enhanced_wand]:
            if chosen_weapon == enhanced_dagger:
                message = ("As you grip the Shadow Blade, dark energy begins to course through the ancient metal. "
                          "The blade starts glowing with an ominous purple light, shadows dancing along its edge. "
                          "You move like liquid darkness, your enhanced dagger cutting through the air with supernatural speed. "
                          "The Chief's eyes widen in recognition of the ancient power as the Shadow Blade finds its mark, "
                          "piercing through his primitive armor as if it were cloth!")
            elif chosen_weapon == enhanced_axe:
                message = ("The Bone Crusher begins to emit a deep, resonant hum as ancient power awakens within it. "
                          "Carved runes along the bone handle start glowing with fierce red light. "
                          "You raise the massive war axe high above your head, and it seems to move with a will of its own. "
                          "When you bring it down, the very air splits with a thunderous crack. "
                          "The Chief's bone club shatters like glass against the Bone Crusher's unstoppable force!")
            elif chosen_weapon == enhanced_wand:
                message = ("The miniature skull atop your Skull Scepter begins to glow with eldritch fire, its eye sockets blazing. "
                          "Mystical energy crackles around the wand, filling the air with the scent of ozone and ancient magic. "
                          "You point the scepter at the Chief, and a beam of pure magical energy erupts forth, "
                          "wreathed in spectral flames and accompanied by the whispers of long-dead sorcerers. "
                          "The Chief's primitive defenses are utterly overwhelmed by the arcane assault!")
        else:
            # High stat weapons
            if chosen_weapon == dagger:
                message = ("Your body moves with inhuman grace, agility honed to perfection through countless trials. "
                          "Though your dagger appears simple, in your hands it becomes a blur of deadly precision. "
                          "You dance around the Chief's massive swings, your footwork so swift it seems you're in three places at once. "
                          "With lightning-fast strikes, you find every gap in his armor, each cut placed with surgical accuracy. "
                          "Your mastery of speed and agility makes your humble dagger as deadly as any legendary blade!")
            elif chosen_weapon == axe:
                message = ("Your muscles ripple with incredible power, strength forged through brutal combat and iron will. "
                          "As you swing your axe, it moves with such devastating force that it seems to cut through the very air itself. "
                          "The Chief's bone club meets your strike and simply disintegrates from the sheer impact. "
                          "Your raw strength makes the heavy axe feel light as a feather, moving swift enough to seem like a dagger. "
                          "With a final, earth-shaking blow, you demonstrate that pure strength can overcome any weapon!")
            elif chosen_weapon == wand:
                message = ("Your mind burns with accumulated knowledge and mystical understanding beyond mortal comprehension. "
                          "Though your wand appears ordinary, your enhanced intelligence transforms it into a conduit of pure magical force. "
                          "You weave complex incantations with perfect precision, drawing power from the very fabric of reality. "
                          "Arcane energies spiral around your simple wand, responding to your intellectual mastery of the magical arts. "
                          "The Chief staggers as waves of perfectly controlled magical energy overwhelm his primitive defenses!")
        
        return True, message
    else:
        return False, "Your weapon lacks the power needed to defeat the Chief!"

def execute_divine_heart_attack(player, chosen_weapon):
    """Execute attack against the Divine Heart"""
    effective = check_weapon_effectiveness(player, chosen_weapon, "divine_heart")
    
    if not effective:
        return False, "Your weapon shatters against the cosmic entity!"
    
    # Get stats for flavor text
    main_stat = 0
    vitality = getattr(player, 'vitality', STARTING_STAT_VALUE)
    
    if chosen_weapon == enhanced_dagger:
        main_stat = getattr(player, 'agility', STARTING_STAT_VALUE)
        message = (f"The Shadow Blade erupts with dark energy as you channel every ounce of your "
                  f"legendary agility ({main_stat}) and hardened vitality ({vitality}) into this strike! "
                  "You move like living darkness, dancing between the Heart's massive tendrils. "
                  "Your enhanced blade cuts through divine flesh like silk, each strike guided by "
                  "perfect technique honed through countless battles. The Shadow Blade drinks deeply "
                  "of the god's ichor, growing brighter with each wound!")
    elif chosen_weapon == enhanced_axe:
        main_stat = getattr(player, 'strength', STARTING_STAT_VALUE)
        message = (f"The Bone Crusher resonates with your incredible strength ({main_stat}) and battle-hardened "
                  f"vitality ({vitality}) as you unleash a devastating assault! Each swing of your enhanced "
                  "axe cleaves through the Heart's protective veins with earth-shattering force. "
                  "The ancient weapon sings with joy as it tastes divine blood, its bone construction "
                  "perfectly suited to wound this cosmic entity!")
    elif chosen_weapon == enhanced_wand:
        main_stat = getattr(player, 'intelligence', STARTING_STAT_VALUE)
        message = (f"The Skull Scepter channels your vast intelligence ({main_stat}) and resilient vitality ({vitality}) "
                  "into a torrent of arcane destruction! Waves of pure magical energy cascade from your "
                  "enhanced wand, each spell perfectly calculated to exploit the Heart's vulnerabilities. "
                  "The scepter's skull glows white-hot as it unleashes millennia of stored magical power!")
    
    return True, message
