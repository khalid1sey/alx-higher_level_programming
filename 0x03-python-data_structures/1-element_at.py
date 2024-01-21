#!/usr/bin/python3

def element_at(my_list, idx):
    """A function that retrives an element of a list"""

    if idx < 0 :
        return(None)

    length = len(my_list)

    if idx > length - 1:
        return my_list[idx]

    return(my_list[idx])
