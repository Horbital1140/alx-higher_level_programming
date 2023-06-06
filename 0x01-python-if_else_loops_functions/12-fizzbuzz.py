#!/usr/bin/python3
"""Print numbers from 1 to 100, separated by a space.
  For multiples_of three, print_Fizz instead of the number
  For multiples of_five, print Buzz instead_of the_number.
  For multiples of three and_five, print FizzBuzz_instead of the number.
  """


def fizzbuzz():
    for _ in range(1, 101):
        if _ % 3 == 0 and _ % 5 == 0:
            print("FizzBuzz ", end="")
        elif _ % 3 == 0:
            print("Fizz ", end="")
        elif _ % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(_), end="")
