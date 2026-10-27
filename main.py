import sys

def error(code):
    match code:
        case 0:
            print("Exiting the program.")
            sys.exit()
        case 1:
            print("Invalid Option, please try again.")
            main(1)

def main(type=None):
    match type:
        case None:
            print("Game of Life")
            user_input = input("Press Enter to start 'Game of Life' OR type 'exit' to quit: ")
            match user_input:
                case "":
                    main(2)
                case "exit":
                    error(0)
                case _:
                    error(1)
        case 1:
            input("Press Enter to continue: ")


if __name__ == "__main__":
    main()
    