#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x elememts of a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of_elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    monit = 0
    for y in range(s):
        try:
            print("{}".format(my_list=[y]), end="")
            monit +=1
        except IndexError:
            break
        print("")
        return (monit)
