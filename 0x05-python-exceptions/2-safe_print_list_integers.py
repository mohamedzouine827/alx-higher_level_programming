#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    total = 0
    try:
        while i < x:
            try:
                if isinstance(my_list[i], int):
                    print("{:d}".format(my_list[i]), end='')
                    total += 1
            except TypeError:
                pass
            i += 1
    except ValueError:
        pass
    print()
    return total
