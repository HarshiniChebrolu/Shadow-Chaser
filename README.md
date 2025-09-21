# Shadow Chaser

### A Survival Maze Game with Limited Visibility — Built with Python & Pygame

---

## 📖 Game Overview

**Shadow Chaser** is an intense survival maze game where the player navigates a randomly generated labyrinth under the constraint of limited visibility. You can only see around yourself within a shrinking circle of light, while the rest of the maze remains shrouded in darkness. Outsmart hazards, collect powerful upgrades, and race against the clock to find the hidden exit before time runs out!

---

## 🔧 Core Gameplay Mechanics

- **Player**  
  - Represented by a yellow circle.  
  - Movement controlled by arrow keys at a base speed.  
  - Visibility limited to a dynamic light radius around the player.

- **Maze Generation**  
  - Procedurally created using a depth-first search (DFS) algorithm.  
  - Walls appear as gray tiles, impassable obstacles.  
  - One green exit tile randomly placed on maze boundaries.

- **Light & Darkness**  
  - Darkness covers the entire maze except a circular area around the player.  
  - Flashlight power-ups temporarily lift darkness to reveal the full map.  
  - Darkness is visually applied as a transparent black overlay with a cutout around the player.

- **Hazards**  
  - **Walls (Gray):** Block movement, cannot be crossed.  
  - **Spikes (Red):** Instant life loss upon contact.  
  - **Enemies (Blue):** Patrol horizontally, cause death on contact.

- **Power-Ups**  
  - **Flashlight (Orange):** Temporarily reveals the entire maze.  
  - **Light Upgrade (White):** Permanently extends player’s light radius.  
  - **Speed Boost (Yellow):** Doubles player speed for a brief time.

- **Enemies**  
  - Programmed with autonomous horizontal movement, reversing on wall collision.  
  - Visible only when inside the player’s light radius.

- **HUD Elements**  
  - Displays current level, remaining lives, death counter, and countdown timer (60 seconds per level).

- **Lives & Deaths**  
  - Player starts with 2 lives across all levels.  
  - Death triggered by spikes, enemies, or timer expiration.  
  - Game Over screen appears upon losing all lives.

---

## 🕹️ Game Flow

1. **Welcome Screen:**  
   - Shows the title and rules of the game; press SPACE to start.

2. **Level Transition:**  
   - Brief level splash screen displaying the current level number.

3. **Gameplay:**  
   - Navigate the maze with limited visibility.  
   - Avoid hazards, collect power-ups, and watch the timer.  
   - Face increasing difficulty with each level as enemies and power-ups grow in number.

4. **Win Condition:**  
   - Reach the green exit before the timer runs out to advance to the next level.

5. **Lose Condition:**  
   - Collision with spikes or enemies, timer hitting zero, and losing all lives results in game over.  
   - Option to restart or quit from Game Over screen.

---

## 🎵 Audio

The game features a continuous looping background track — *“mission_impossible.mp3”* — to keep the suspense and intensity alive throughout gameplay.

---

## ⚙️ Code Structure

- **Global Setup:**  
  Initializes Pygame, audio mixer, display, global variables, and game state parameters.

- **Enemy Class:**  
  Manages enemy movement, rendering, and interaction limited to player’s visible area.

- **Screen Functions:**  
  - `show_welcome_screen()` — Displays intro and instructions.  
  - `show_game_over()` — Displays game over menu with restart and quit options.  
  - `show_level_transition()` — Displays level start screen.

- **Maze Functions:**  
  - `generate_maze_with_walls()` — Generates maze layout using DFS.  
  - `draw_maze()` — Renders maze components with lighting and visibility effects.

- **Gameplay Logic:**  
  - `play_level(level_idx)` — Main game loop per level handling movement, collisions, power-ups, enemies, HUD, and win/lose conditions.

- **Main Loop:**  
  Coordinates screen flows: welcome → levels → game over or restart.

---

## 🏁 Summary

**Shadow Chaser** offers a thrilling maze survival experience featuring:

- Innovative limited visibility gameplay creating tension and challenge.  
- Randomized maze layouts for replayability.  
- Strategic use of power-ups affecting light and speed.  
- Enemies and hazards encouraging careful navigation.  
- Timed challenges pushing player skill and speed.

It is a complete mini-game project in Python showcasing:

- Maze generation algorithms (DFS).  
- Collision detection and game physics.  
- Dynamic game loop and HUD management.  
- Integration of audio and visual effects.  
- Object-oriented design for enemies and game entities.

---

## 🚀 How to Run

1. Install dependencies:

