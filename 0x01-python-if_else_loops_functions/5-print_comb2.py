#!/usr/bin/python3

for _ in range(100):
    print(f"{_:02d}", end=(", " if _ != 99 else "\n"))

