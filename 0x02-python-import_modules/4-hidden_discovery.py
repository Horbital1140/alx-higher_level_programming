#!/usr/bin/python3

if __name__ == "__main__":
    """Print all name_s defined_by hidden_4 module."""
    import hidden_4

    name_s = dir(hidden_4)
    for name in name_s:
        if name[:2] != "__":
            print(name)
