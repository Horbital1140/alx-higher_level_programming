#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum of all arguments. cast the arguement to integer"""
    import sys

    total = 0
    for _ in range(len(sys.argv) - 1):
        total += int(sys.argv[_ + 1])
    print("{}".format(total))
