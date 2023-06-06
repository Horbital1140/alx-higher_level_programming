#!/usr/bin/python3
"""Print all the ASCII alphabet in lowercase
NO new line."""

for _ in range(97, 123):
    print("{}".format(chr(_)), end="")
