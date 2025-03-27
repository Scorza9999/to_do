import os
from pathlib import Path  # Cross-platform paths
import platform
from sys import argv


# Positional only function
def ask_int(msg: str, min_limit: int, max_limit: int, /) -> int:
    """ 
    Ask the user for the operation

    Asks the user for the operation they want to do and warns them if they
    inputted an impossible value
    """
    while True:
        try:
            n: int = int(input(msg))
            if min_limit <= n <= max_limit:
                return n
            else:
                print(f"You must insert a number between {min_limit} and {max_limit}.")
        except ValueError:
            print("You must insert a number.")


# Pretty self-explaining function name
def clear_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


# Ideally we should tell the user that they already need a text file or provide
# an option to create one
if len(argv) == 1:
    raise SystemExit("You need to provide a text file.")

file_path: Path = Path(argv[1])
# Am i catching all errors?
try:
    with file_path.open(encoding="utf-8", errors="replace") as f:
        to_do_list: list[str] = f.readlines()
except FileNotFoundError:
    # TODO: implement
    raise NotImplementedError("Creation not implemented.")
except PermissionError:
    raise SystemExit("Failed to open file. Permission denied.")
except OSError as e:
    raise SystemExit(f"Failed to open file. {e}.")

# TODO: check if list is valid?

try:
    while True:
        clear_terminal()
        print("0) Exit", "1) Add", "2) Remove", "3) Rename", sep=" \n")
        print ("4) Toggle \n")

        if to_do_list == []:
            print("Empty")
        else:
            for to_do in to_do_list:
                print(to_do, end="")  # To-dos already end with a newline

        choice: int = ask_int("Choose an option: ", 0, 4)
# I believe that a match statement is more elegant than a bunch of if and elif
# statements, in the case you disagree and/or there is a performance hit, I 
# only commented the previous lines out.

#        if choice == 0:
 #           break
  #      elif choice == 1:
            # input() function already returns a string
   #         name = input("Insert name: ")
    #        to_do_list.append(f"[ ] {name}\n")       
        match choice:
            case 0:
                break
            case 1:
                name = input("Insert name: ")
                to_do_list.append(f"[ ] {name}\n")
            case _:
                print("not implemented yet!")

except KeyboardInterrupt:
    pass

# TODO save before exiting
