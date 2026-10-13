# Import the random module so the robot can make random moves.
import random

# Constants and setup
# Starting position of the robot on the grid.
INITIAL_POSITION = (2, 2)

# Goal position where the robot wants to arrive.
GOAL_POSITION = (4, 4)

# Cells that contain obstacles. The robot cannot move into these cells.
OBSTACLES = [(3, 3), (4, 2), (2, 4)]

# Directions the robot can move.
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'

# Maze symbols:
# Obstacles = "O"
# Empty space = "S"
# Initial Position = "I"
# Goal Position = "G"

# Create a dictionary called maze to represent the grid.
# Each key is a coordinate like (x, y), and each value is a symbol.
maze = {}
for x in range(1, 6, 1):
    for y in range(1, 6, 1):
        if (x, y) in OBSTACLES:
            maze[(x, y)] = "O"
        elif (x, y) == INITIAL_POSITION:
            maze[(x, y)] = "I"
        elif (x, y) == GOAL_POSITION:
            maze[(x, y)] = "G"
        else:
            maze[(x, y)] = "S"


# Display the welcome screen and maze map

def display_welcome_message():
    print("""

    ▓   ▓ ▓▓▓  ▓▓▓  ▓▓▓▓   ▓▓▓  ▓   ▓  ▓▓▓  ▓▓▓▓▓ ▓▓▓▓▓ 
    ▓▓ ▓▓  ▓  ▓     ▓   ▓ ▓   ▓ ▓▓ ▓▓ ▓   ▓    ▓  ▓     
    ▓ ▓ ▓  ▓  ▓     ▓▓▓▓  ▓   ▓ ▓ ▓ ▓ ▓▓▓▓▓   ▓   ▓▓▓▓  
    ▓   ▓  ▓  ▓     ▓  ▓  ▓   ▓ ▓   ▓ ▓   ▓  ▓    ▓     
    ▓   ▓ ▓▓▓  ▓▓▓  ▓   ▓  ▓▓▓  ▓   ▓ ▓   ▓ ▓▓▓▓▓ ▓▓▓▓▓ 
    """)

    print("Welcome to the Robot Simulation Program!")

    print("""
     
     Y Axis
     ^
     |  ||===================||
     |  ||   |   |   |   |   ||
     |  ||-------------------||
     |  ||   | O |   | G |   ||
     |  ||-------------------||
     |  ||   |   | O |   |   ||
     |  ||-------------------||
     |  ||   | I |   | O |   ||
     |  ||-------------------||
     |  ||   |   |   |   |   ||
     |  ||===================||
     |
     + -------------------------> X Axis
    """)

    print("Legend:")
    print("I: Initial Position")
    print("G: Goal Position")
    print("O: Obstacle")


# Run the simulation many times
# This function repeats the robot's random movement many times.
# It stores the path that reached the goal in the fewest steps.
def run_simulations(number_of_simulations=10000):
    # Keep track of the best result found so far.
    lowest_steps = None
    lowest_actions = []
    lowest_run = None

    # Run the simulation many times.
    for run_number in range(1, number_of_simulations + 1):
        # start_robot() returns how many steps it took and the list of actions taken.
        steps, actions = start_robot(record_path=True)

        # If this run is better than the current best, save it.
        if lowest_steps is None or steps < lowest_steps:
            lowest_steps = steps
            lowest_actions = actions
            lowest_run = run_number

    # Create a dictionary to convert direction letters into readable names.
    action_names = {
        NORTH: "North",
        EAST: "East",
        SOUTH: "South",
        WEST: "West",
    }

    # Convert the list of movement letters into a readable sentence like:
    # North -> East -> South
    best_path = " -> ".join(
        action_names[action]
        for action in lowest_actions
    )

    # Print the result of the best simulation.
    print(f"\nLowest number of steps: {lowest_steps} (run {lowest_run})")
    print(f"Actions in the lowest-step run: {best_path}")

    # Return the best result for possible later use.
    return lowest_steps, lowest_actions


# Start one robot simulation
# This function moves the robot until it reaches the goal.
def start_robot(record_path):
    # Reset the robot to its starting position for one new run.
    current_position = INITIAL_POSITION
    steps = 0
    actions = []

    # Keep moving until the robot reaches the goal.
    while current_position != GOAL_POSITION:
        # Pick a random number from 1 to 4 to choose a direction.
        action_number = random.randint(1, 4)

        # Convert the random number into a movement direction.
        if action_number == 1:
            action = NORTH
        elif action_number == 2:
            action = EAST
        elif action_number == 3:
            action = SOUTH
        else:
            action = WEST

        # Try to move the robot in that direction.
        new_position = move(action, current_position)

        # Record the action and update the robot's position.
        actions.append(action)
        current_position = new_position
        steps += 1

    # If record_path is True, return both the steps and the action list.
    if record_path:
        return steps, actions

    # Otherwise, return only the number of steps.
    return steps


# Move the robot in a chosen direction
# This function checks whether the next position is valid.
# If it is inside the maze and not an obstacle, the robot can move there.
def move(a, current_position):
    x, y = current_position

    # Calculate the robot's next position based on the chosen direction.
    if a == NORTH:
        new_position = (x, y + 1)
    elif a == EAST:
        new_position = (x + 1, y)
    elif a == SOUTH:
        new_position = (x, y - 1)
    elif a == WEST:
        new_position = (x - 1, y)
    else:
        new_position = (x, y)

    # If the new position is inside the maze and is not an obstacle,
    # allow the move. Otherwise, keep the robot in its current spot.
    if new_position in maze and maze[new_position] != "O":
        return new_position
    else:
        return current_position


# Run the program when the file starts.
display_welcome_message()
run_simulations()

