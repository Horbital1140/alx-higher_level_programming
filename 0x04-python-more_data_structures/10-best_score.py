#!/usr/bin/python3


def best_score(a_dictionary):
    """
    A function that returns a key with the biggest integer value.
    """
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        score = 0
        leader_s = ""
        for i in my_list:
            if a_dictionary[i] > score:
                score = a_dictionary[i]
                leader_s = i
        return leader_s
