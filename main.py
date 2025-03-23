import os
from pathlib import Path  # Cross-platform paths
import platform
from sys import argv


def ask_int(msg: str, min_limit: int, max_limit: int) -> int:
    while True:
        try:
            n: int = int(input(msg))
            if min_limit <= n <= max_limit:
                return n
            else:
                print(f"You must insert a number between {min_limit} and {max_limit}.")
        except ValueError:
            print("You must insert a number.")


def clear_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


if len(argv) == 1:
    raise SystemExit("You need to provide a file.")

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
        print("0) Exit")
        print("1) Add")
        print("2) Remove")
        print("3) Rename")
        print("4) Toggle")
        print()

        if to_do_list == []:
            print("Empty")
        else:
            for to_do in to_do_list:
                print(to_do, end="")  # To-dos already end with a newline

        choice: int = ask_int("Choose an option: ", 0, 4)
        if choice == 0:
            break
        elif choice == 1:
            name: str = input("Insert name: ")
            to_do_list.append(f"[ ] {name}\n")
except KeyboardInterrupt:
    pass

# TODO save before exiting
