# Level Progression, Revisit Rules, and Gating

This document summarizes the current level map, key prerequisites, and revisit behavior.

## Core Progression
- cave_entrance → skull_chamber → cave_in → primitive_village
- From primitive_village:
  - alley (combat → Armory Key)
  - armory (requires Armory Key)
  - chiefs_house (requires Chief's House Key; obtained via armory)
- chiefs_house can guide to healing_pool → village_changed

## Prerequisites
- armory: requires "Armory Key"
- chiefs_house: requires "Chief's House Key"

## Combat Zones
- Combat is currently allowed only in: alley

## Revisit Behavior
- Revisit generally allowed unless gated by prerequisites.
- Example: You may return to primitive_village from armory and chiefs_house.

## Validation
- A runtime continuity validator enforces the rules above after each consequence.
- Invalid transitions are reverted to primitive_village with a message.

## Source of Truth
- `docs/level_map.json`: generated via `utilities/generate_level_map.py` and enriched with rules by `utilities/inject_rules.py`.
- Visual graph: `docs/level_graph.dot` (and `level_graph.png` if Graphviz is installed).

## Regression
- Run full check: `python utilities/regression.py`
  - Generates level map, injects rules, runs autoplay through a representative route.


