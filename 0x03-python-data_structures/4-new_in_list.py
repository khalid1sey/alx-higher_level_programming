#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if not my_list:
        return (my_list)

    length = len(my_list)

    if idx > length - 1:
        return (my_list)

    my_list[idx] = element

    return (my_list)
