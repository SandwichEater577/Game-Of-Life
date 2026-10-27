import sys

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
    new_grid = [[""] * cols for _ in range(rows)]
    return new_grid

def render_grid(grid):
    for row in grid:
        for cell in cell:
            if cell == 1:
                print("█", end="")
            else:
                print(" ", end="")
        print()

def main():
    handle_program_start()
    grid = create_grid(20, 20) # (Height, Width)
    program_running = True
    while program_running:
        render_grid(grid)

if __name__ == "__main__":
    main()