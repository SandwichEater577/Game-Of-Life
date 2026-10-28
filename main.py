import sys
import os
import time

game_of_life_rules = (
    "Underpopulation: A live cell with fewer than 2 live neighbors dies.",
    "Survival: A live cell with 2 or 3 live neighbors survives to the next generation.",
    "Overpopulation: A live cell with more than 3 live neighbors dies.",
    "Reproduction: A dead cell with exactly 3 live neighbors becomes a live cell.",
)

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
        "min_size": (10, 3),
        "pattern": [
            [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0],
            [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
            [0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0]
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

def handle_program_start(type=None):
    match type:
        case None:
            while True:
                print("Game of Life (Wrote on Python 3.14.8)")
                user_input = input("Press Enter to start 'Game of Life' OR type 'exit' to quit: ")
                match user_input:
                    case "":
                        handle_program_start(2)
                        return 
                    case "exit":
                        error(0)
                    case _:
                        error(1)
        case 1:
            input("Press Enter to continue: ")
            handle_program_start(2)
        case 2:
            return 

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
        print("If you want to finish placing cells, press Enter without typing anything.")

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
        for c in range(len(pattern)): 
            if pattern[r][c] == 1:
                grid_r = offset_row + r
                grid_c = offset_col + c
                
                if 0 <= grid_r < len(grid) and 0 <= grid_c < len(grid[0]):
                    grid[grid_r][grid_c] = 1

def show_and_pick_patterns(grid):
    ...

def display_game_options(grid):
    os.system("clear")
    render_grid(grid)
    print("============================")
    print("Welcome to the Game of Life!")
    print("============================")
    print("Options:")
    print("1. Place cells manually")
    print("2. Pick from existing patterns (Default)")
    print("3. See the rules of Game of Life")
    print("4. Exit the program")
    print("============================")

    while True:
        try:
            user_input = int(input("Enter an option (1-4): ") or 2)
        except ValueError:
            error(1)
            continue

        match user_input:
            case 1:
                ask_user_for_cell_placement(grid)
                break
            case 2:
                show_and_pick_patterns(grid)
                break
            case 3:
                show_rules()
                break
            case 4:
                error(0)
                break
            case _:
                error(1)

def main():
    handle_program_start()

    cols = int(input("Enter columns count (Width in cells)(Default: 20): ")or 20)
    rows = int(input("Enter rows count (Height in cells)(Default: 20): ")or 20)
    
    grid = create_grid(rows, cols) # (Height, Width)

    display_game_options(grid)

    program_running = True

    try:
        while program_running:
            os.system("clear")
            render_grid(grid)
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("\n \n Exiting Game of Life... \n \n")
        sys.exit()

if __name__ == "__main__":
    main()