#!/usr/bin/python3

b = 0
for _ in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(_ - b)), end="")
    b = 32 if b == 0 else 0
