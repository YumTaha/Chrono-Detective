# Chrono-Detective

An unfinished Python/Pygame game prototype built around a time-travel detective concept.

## Project status

The current code implements a basic player-and-enemy game loop, enemy pursuit, and health loss on collisions. The historical investigations, clues, puzzles, and branching story described below are design ideas, not completed gameplay features.

## Run the prototype

Requires Python 3 and a graphical desktop.

```bash
git clone https://github.com/YumTaha/Chrono-Detective.git
cd Chrono-Detective
python -m pip install pygame
python main.py
```

Close the window to exit. This early prototype may need further development.

## Original concept

A detective travels between historical eras, such as Ancient Egypt, Medieval Europe, and the Wild West, to gather clues and solve crimes. Planned mechanics include deduction, puzzles, mini-games, and choices that can affect the story or create time-travel paradoxes.

## Repository guide

- `main.py` — initialization, game loop, enemies, and collision handling.
- `player.py` — player behavior.
- `enemy.py` — enemy behavior.
- `settings.py` — game configuration.
- `debug.py` — debugging helpers.
