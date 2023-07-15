#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for value_dico in list_keys:
        if value == a_dictionary.get(value_dico):
            del a_dictionary[value_dico]

    return (a_dictionary)
