#!/usr/bin/python3
"""
The two digits must be different - 01 and 10 are considered identical
"""
for dualnumb1 in range(0, 10):
    for dualnumb2 in range(dualnumb1 + 1, 10):
        if dualnumb1 == 8 and dualnumb2 == 9:
            print("{}{}".format(dualnumb1, dualnumb2))
        else:
            print("{}{}".format(dualnumb1, dualnumb2), end=", ")
