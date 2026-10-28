import sys
import os
import time

game_of_life_rules = (
    "Underpopulation: A live cell with fewer than 2 live neighbors dies.",
    "Survival: A live cell with 2 or 3 live neighbors survives to the next generation.",
    "Overpopulation: A live cell with more than 3 live neighbors dies.",
    "Reproduction: A dead cell with exactly 3 live neighbors becomes a live cell.",
)

# Patterns taken from: https://en.wikipedia.org/wiki/Conway's_Game_of_Life 
PATTERNS = [
    {
        "name": "Blinker",
        "min_size": (3, 3),
        "pattern": [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]   
    },
    {
        "name": "Toad",
        "min_size": (4, 4),
        "pattern": [
            [0, 1, 1, 1],
            [1, 1, 1, 0]
        ]
    },
    {
        "name": "Beacon",
        "min_size": (4, 4),
        "pattern": [
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1]
        ]
    },
    {
        "name": "Pulsar",
        "min_size": (13, 13),
        "pattern": [
            [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]
        ]
    },
    {
        "name": "Penta-decathlon",
        "min_size": (16, 9),
        "pattern": [
            [1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1],
            [1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1],
            [1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1]
        ]
    }
]

def error(code):
    match code:
        case 0:
            print("Exiting the program.")
            sys.exit()
        case 1:
            print("Invalid Option, please try again.")
        case 2:
            print("Cell placement is out of bounds.")
        case 3:
            print("Invalid format! Please use 'row, col' (e.g., 5, 5).")

def handle_program_start():
    while True:
        print("Game of Life (Wrote on Python 3.14.8)")
        user_input = input("Press Enter to start 'Game of Life' OR type 'exit' to quit: ")
        if user_input == "":
            return
        elif user_input == "exit":
            error(0)
        else:
            error(1)

def create_grid(rows, cols): # (Height, Width)
    new_grid = [[0] * cols for _ in range(rows)]
    return new_grid

def render_grid(grid):
    width = len(grid[0])

    # ASCII chars taken from: https://www.asciiart.eu/ascii-borders/maker
    print("╔" + "═" * width + "╗") 
    
    for row in grid:
        print("║", end="")
        for cell in row:
            if cell == 1:
                print("█", end="")
            else:
                print(" ", end="")
        print("║")
    print("╚" + "═" * width + "╝")

def put_cell(grid, row, col):
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        if grid[row][col] == 0:
            grid[row][col] = 1
        else:
            grid[row][col] = 0
    else:
        error(2)

def ask_user_for_cell_placement(grid):
    while True:
        os.system("clear")
        render_grid(grid)

        print("\n Type coordinates to place a cell (row, col)")
        print("If u want to preview the grid, type 'p' and press Enter.")
        print("If the cell is already alive, it will be exterminated.")
        print("EXAMPLE: 10, 10")
        print("Press Enter without typing anything to go back to the menu.")

        user_input = input("> ")

        if user_input == "":
            break
        if user_input == "p":
            os.system("clear")
            render_grid(grid)
            input("\nPress Enter to return to placement mode...")
            continue

        try:
            parts = user_input.split(",")
            row = int(parts[0].strip())
            col = int(parts[1].strip())
            put_cell(grid, row, col)
        except (ValueError, IndexError):
            error(3)
            time.sleep(1.5)

def show_rules():
    os.system("clear")
    print("============================")
    print("Rules of Game of Life:")
    print("============================")
    for rule in game_of_life_rules:
        print(rule)
    print("============================")
    input("\nPress Enter to return to the main menu...")

def push_pattern_to_grid(grid, pattern_dict, offset_row, offset_col):
    pattern = pattern_dict["pattern"]
    for r in range(len(pattern)):
        for c in range(len(pattern[0])): 
            if pattern[r][c] == 1:
                grid_r = offset_row + r
                grid_c = offset_col + c
                if 0 <= grid_r < len(grid) and 0 <= grid_c < len(grid[0]):
                    grid[grid_r][grid_c] = 1

def show_and_pick_patterns(grid, patterns=PATTERNS):
    os.system("clear")
    print("============================")
    print("Available Patterns:")
    print("============================")
    for i, p in enumerate(patterns):
        print(f"{i + 1}. {p['name']}")
    print("0. Go back")

    try:
        choice = int(input("\nPick a number: "))
        if choice == 0:
            return
        selected_pattern = patterns[choice - 1]

        os.system("clear")
        render_grid(grid)
        print(f"\nWhere do you want to place the {selected_pattern['name']}?")
        row = int(input("Enter the starting row (0-indexed): "))
        col = int(input("Enter the starting column (0-indexed): "))

        push_pattern_to_grid(grid, selected_pattern, row, col)
        time.sleep(1.5)
    except (ValueError, IndexError):
        error(3)
        time.sleep(1.5)

def display_game_options(grid):
    while True: 
        os.system("clear")
        render_grid(grid)
        print("============================")
        print("Welcome to the Game of Life!")
        print("============================")
        print("Options:")
        print("1. Place cells manually")
        print("2. Pick from existing patterns (Default)")
        print("3. See the rules of Game of Life")
        print("4. Start game")
        print("5. Exit the program")
        print("============================")

        try:
            user_input = int(input("Enter an option (1-5): ") or 2)
        except ValueError:
            error(1)
            time.sleep(1.5)
            continue

        match user_input:
            case 1:
                ask_user_for_cell_placement(grid)
            case 2:
                show_and_pick_patterns(grid)
            case 3:
                show_rules()
            case 4:
                break
            case 5:
                print("Exiting...")
                sys.exit()
            case _:
                error(1)
                time.sleep(1.5)

def count_neighbors(grid, row, column):
    count = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            nr = (row + dr) % len(grid)
            nc = (column + dc) % len(grid[0])
            if grid[nr][nc] == 1:
                count += 1
    return count

def next_generation(grid):
    new_grid = create_grid(len(grid), len(grid[0]))
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            neighbors = count_neighbors(grid, r, c)
            current_cell = grid[r][c]
            
            if current_cell == 1 and (neighbors == 2 or neighbors == 3):
                new_grid[r][c] = 1
            elif current_cell == 0 and neighbors == 3:
                new_grid[r][c] = 1
    return new_grid

def main():
    handle_program_start()

    while True:
        try:
            cols = int(input("Enter columns count (Width in cells)(Default: 20): ") or 20)
            rows = int(input("Enter rows count (Height in cells)(Default: 20): ") or 20)
            if cols <= 0 or rows <= 0:
                print("Error: Grid size must be greater than 0.")
                time.sleep(1.5)
                continue
            break
        except ValueError:    
            print("Invalid input, please enter a number.")
            time.sleep(1.5)

    grid = create_grid(rows, cols) # (Height, Width)

    display_game_options(grid)

    program_running = True

    try:
        while program_running:
            os.system("clear")
            render_grid(grid)
            time.sleep(0.2)
            grid = next_generation(grid)
    except KeyboardInterrupt:
        print("\n \n Exiting Game of Life... \n \n")
        sys.exit()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n \n Program terminated by user. \n \n")
        sys.exit()