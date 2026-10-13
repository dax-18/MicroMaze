# Robot Simulation Program

A simple Python-based robot navigation simulation that explores a 5x5 maze, avoids obstacles, and attempts to find the shortest successful route from the starting position to the goal.

## Project Overview

This project simulates a robot moving randomly through a grid. The robot begins at the initial position and keeps moving until it reaches the goal cell. The program repeats this simulation many times, records the path taken, and reports the run with the fewest steps.

The maze includes:
- A start position
- A goal position
- Several blocked obstacle cells
- Valid movement in four directions: North, East, South, and West

## Features

- 5x5 grid-based maze representation
- Obstacle detection to prevent invalid moves
- Randomized robot movement simulation
- Repeated runs to estimate the best path
- Display of the maze layout and legend
- Output of the shortest recorded path in terms of steps

## Maze Layout

The robot operates in the following environment:

- Start position: (2, 2)
- Goal position: (4, 4)
- Obstacles: (3, 3), (4, 2), (2, 4)

## How It Works

The program uses a dictionary mapping each coordinate to a symbol:
- I = Initial position
- G = Goal position
- O = Obstacle
- S = Empty space

Each simulation:
1. Resets the robot to the start position
2. Chooses a random direction
3. Moves if the target cell is valid and not blocked
4. Repeats until the goal is reached
5. Stores the number of steps and the move sequence

After multiple simulations, the program compares all runs and prints the path with the least number of moves.

## Running the Program

Make sure Python is installed, then run:

```bash
python main.py
```

## Example Output

The program prints:
- A welcome screen
- The maze map with legend
- The best path found after repeated simulations
- The lowest number of steps and the movement sequence

## Files

- `main.py` — contains the simulation logic and execution code
- `README.md` — project documentation

## Notes

This is a basic simulation designed for learning robotic path movement and simple maze navigation logic. It demonstrates how random movement can be evaluated over repeated trials to identify a relatively efficient path in a constrained environment.
