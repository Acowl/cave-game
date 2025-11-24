# Game Design: Shabuya Real-Time

## Core Concept
Transition from a turn-based text adventure to a **2D Top-Down Action RPG** (Zelda-lite style).

## Tech Stack
- **Language**: Python 3.10+
- **Engine**: `pygame-ce` (Community Edition - faster/better maintained)
- **Architecture**: Entity-Component-System (ECS) or standard OOP Game Loop.

## Mechanics
| Feature | Old (Turn-Based) | New (Real-Time) |
| :--- | :--- | :--- |
| **Movement** | Menu choices ("Go North") | WASD/Arrow Keys |
| **Combat** | Select "Attack" -> Calculation | Spacebar to swing sword, collision detection |
| **Enemies** | Static encounters | Roaming AI, chasing player |
| **World** | Text descriptions | Tile-based maps (using Tiled or simple arrays) |

## Asset Plan
- Reuse existing `.png` assets in `cave-game/assets/sprites`.
- Create a `SpriteManager` class to handle animations.
