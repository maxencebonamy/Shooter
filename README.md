# Shooter

A side-scrolling 2D shooter written in Python with Pygame.

Fly a ship across a scrolling background, shoot the monsters coming from the right and avoid colliding with them. The game ends when a monster leaves the screen on the left or when the ship is destroyed.

## Table of contents

- [Shooter](#shooter)
	- [Table of contents](#table-of-contents)
	- [How it works](#how-it-works)
	- [Tech stack](#tech-stack)
	- [Repository structure](#repository-structure)
	- [Prerequisites](#prerequisites)
	- [Installation](#installation)
	- [Running locally](#running-locally)
	- [Useful scripts](#useful-scripts)
	- [License](#license)

## How it works

1. **Controls**: the arrow keys move the ship, `Space` fires, `A` quits the game. The ship cannot leave the window.
2. **Monsters**: three monsters are kept on screen at all times. They spawn just past the right edge at a random height and move left.
3. **Shooting**: a projectile hitting a monster destroys it, plays an explosion and adds 1 to the score. A new projectile can only be fired once the previous one is at least 35 pixels ahead of the ship.
4. **Collision**: if a monster touches the ship, both explode and the ship is removed.
5. **Game over**: the game ends when a monster reaches the left edge, or when the ship is destroyed and its explosion has finished. The window then closes.

## Tech stack

| Layer | Technologies |
| --- | --- |
| Language | Python 3.9 |
| Game engine | Pygame 2.6.1 |
| Assets | PNG sprites, `beware.ttf` font |
| Tooling | `venv`, shell launcher (`run.sh`) |

## Repository structure

```
.
├── assets/       Sprites (player, monsters, projectile, explosion, background) and font
├── const/        Game constants (window size, speeds, FPS, monster count)
├── display/      Window creation and per-frame rendering
├── event/        Keyboard, mouse and quit event handling
├── game/         Game logic and entities (player, monster, projectile, blast, score, wallpaper)
├── main.py       Entry point and main loop
└── run.sh        Launcher using the local virtual environment
```

Each entity class loads its own image from `assets/` and exposes a `display` method that moves and draws it for the current frame. Tunable values such as `PLAYER_SPEED`, `MONSTER_SPEED`, `MONSTER_COUNT` and `GAME_FPS` are defined in `const/const.py`. Asset paths are relative, so the game must be started from the repository root.

## Prerequisites

- [Python](https://www.python.org/) 3.9 (the version of the local virtual environment)
- A display able to open a 800x400 window

## Installation

The repository does not ship a dependency file. Create a virtual environment and install Pygame:

```bash
python3 -m venv .venv
.venv/bin/pip install pygame==2.6.1
```

## Running locally

```bash
./run.sh
```

Or without the launcher:

```bash
.venv/bin/python main.py
```

## Useful scripts

| Command | Effect |
| --- | --- |
| `./run.sh` | Start the game with the interpreter from `.venv` |
| `.venv/bin/python main.py` | Start the game directly |

## License

This project is licensed under the [MIT License](LICENSE).
