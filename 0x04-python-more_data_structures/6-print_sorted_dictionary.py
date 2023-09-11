#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    """
    A function that prints_a dictionary by ordered_keys
    """
    keys = list(a_dictionary.keys())
    keys.sort()
    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
