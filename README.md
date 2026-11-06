# Conway's Game of Life

A terminal-based implementation of Conway's Game of Life, written in Python.

## Overview

Conway's Game of Life is a zero-player cellular automaton created by mathematician John Conway. It runs on a grid where each cell is either alive or dead. Every generation, cells update their state based on the number of living neighbours around them.

Despite having only four simple rules, these interactions can produce surprisingly complex patterns, from stable structures to continuously moving formations.

This project brings the simulation directly to the terminal. It uses ASCII and Unicode block characters to render the grid, with an interactive menu for editing the world, loading predefined patterns, and controlling the simulation.

The world uses wrap-around boundaries, meaning cells leaving one edge reappear on the opposite side. This effectively turns the grid into a torus.

## Features

- **Interactive menu** — Create, remove, and manage cells without editing the source code.
- **Pattern library** — Includes predefined patterns such as Blinker, Toad, Pulsar, and Penta-decathlon.
- **Custom grid dimensions** — Choose the size of the simulation before starting.
- **Real-time simulation** — Watch generations update automatically in the terminal.
- **Toroidal boundaries** — Movement across the edges of the grid is seamless.
- **Terminal rendering** — Uses ASCII and Unicode block characters for a clean console interface.

## Screenshots

|             Main Menu             |                 Available Patterns                  |
| :-------------------------------: | :-------------------------------------------------: |
| ![Main Menu](Images/MainMenu.png) | ![Available Patterns](Images/AvailablePatterns.png) |

**Penta-decathlon preview**

![Penta-decathlon](Images/Penta-DecathlonPreview.png)

## How it works

Each cell follows four rules:

1. **Underpopulation** — A living cell with fewer than two living neighbours dies.
2. **Survival** — A living cell with two or three living neighbours survives.
3. **Overpopulation** — A living cell with more than three living neighbours dies.
4. **Reproduction** — A dead cell with exactly three living neighbours becomes alive.

All cells update simultaneously, producing the next generation.

## Getting started

### Requirements

- Python 3.10 or newer.
- A terminal that supports ANSI escape sequences.

No external Python packages are required.

### Installation

You can either download the source code or grab the precompiled Windows executable from the [Releases](../../releases) page.

To download the repository:

```bash
git clone <repository-url>
cd <repository-folder>
```

### Running

Start the program with:

```bash
python main.py
```

The interactive menu will guide you through setting up and running the simulation.

## Troubleshooting

**Terminal keeps printing new screens instead of clearing**

Some terminals may not handle the default screen-clearing command correctly.

Replace:

```python
os.system("clear")
```

With:

```python
print("\033c", end="")
```

**SyntaxError when starting the program**

Make sure you're running Python 3.10 or newer. Earlier versions don't support the `match/case` syntax used in this project.

## License

This project is licensed under the MIT License. See [LICENSE.md](LICENSE.md) for details.
