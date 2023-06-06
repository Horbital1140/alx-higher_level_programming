#!/usr/bin/python3
for _ in range(0, 100):
    if _ == 99:
        print("{}".format(_))
    else:
        print("{:02}".format(_), end=", ")
