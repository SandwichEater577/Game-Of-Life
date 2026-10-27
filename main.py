import sys
import os
import time

def error(code):
    match code:
        case 0:
            print("Exiting the program.")
            sys.exit()
        case 1:
            print("Invalid Option, please try again.")

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

    print("╔" + "═" * width + "╗") # ASCII chars taken from: https://www.asciiart.eu/ascii-borders/maker
    
    for row in grid:
        print("║", end="")
        for cell in row:
            if cell == 1:
                print("█", end="")
            else:
                print(" ", end="")
        print("║")
    print("╚" + "═" * width + "╝")

def main():
    handle_program_start()

    cols = int(input("Enter columns count (Width in cells)(Default: 20): ")or 20)
    rows = int(input("Enter rows count (Height in cells)(Default: 20): ")or 20)
    
    grid = create_grid(rows, cols) # (Height, Width)


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