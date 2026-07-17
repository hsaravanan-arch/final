# Snake Game

## Description

The  Snake Game is a game which I created using Python and the Pygame library.

The user controls the snake using the arrow keys. The goal is to eat the moving food while avoiding the walls, obstacles, and the snake's own body.

Each time the snake eats the food:
- The score increases by 1.
- The snake grows longer.
- The food moves to a new random location.
- The food changes to a random color and direction.

## Features

- snake is controlled by the arrow keys.
- Randomly moving food that changes color.
- Snake grows longer after eating food.
- Score tracker displayed on the screen.
- Colorful obstacles that the snake must avoid.
- Collision detection for walls, obstacles, and the snake's body.
- Game Over screen with the final score.
- Restart the game by pressing **R**.
- Quit the game by pressing **Q**.

## Installation

### Requirements

Before running the game, make sure you have:

- Python 3 installed.
- Pygame installed.

Install Pygame by running:

```bash
pip install pygame
```

If that does not work, use:

```bash
python3 -m pip install pygame
```

## How to Run

1. Download or clone this repository.

2. Open the project folder.

3. Open a terminal in the project folder.

4. Run the game using:

```bash
python3 snake_game.py
```

If that does not work, use:

```bash
python snake_game.py
```

The Snake Game window will open, and you can begin playing.
## Controls

| Key | Action |
|------|--------|
| ↑ | Move Up |
| ↓ | Move Down |
| ← | Move Left |
| → | Move Right |
| R | Restart the game after Game Over |
| Q | Quit the game after Game Over |
## Project Structure

```
Snake_Game/
│
├── snake_game.py
└── README.md
```
## Future Improvements

In the future, I would like to:

- Add sound effects and background music.
- Add different difficulty levels.
- Save the highest score.
- Add more obstacle layouts.
- Increase the snake speed as the score increases.
- Add different game backgrounds.
