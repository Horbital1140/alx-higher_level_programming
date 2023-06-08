#!/usr/bin/python3

if __name__ == "__main__":
    """Print_the number_of_and list_of arguments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for _ in range(count):
        print("{}: {}".format(_ + 1, sys.argv[_ + 1]))
