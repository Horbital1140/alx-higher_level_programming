#!/usr/bin/python3
"""Print all the ASCII alphabet in lowercase
NO new line."""

for _ in range(ord('a'), ord('z') + 1):
    print(chr(_), end='')

