import sys

def error(code):
    match code:
        case 0:
            print("Exiting the program.")
            sys.exit()
        case 1:
            print("Invalid Option, please try again.")
            handle_program_start(1)

def handle_program_start(type=None):
    match type:
        case None:
            print("Game of Life (Wrote on Python 3.14.8)")
            user_input = input("Press Enter to start 'Game of Life' OR type 'exit' to quit: ")
            match user_input:
                case "":
                    handle_program_start(2)
                case "exit":
                    error(0)
                case _:
                    error(1)
        case 1:
            input("Press Enter to continue: ")
            handle_program_start(2)
        case 2:
            main()

def main():
    handle_program_start()
    

if __name__ == "__main__":
    main()