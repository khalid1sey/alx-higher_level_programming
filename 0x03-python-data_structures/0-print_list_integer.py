#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """A function to print all integers of a list."""
    if not my_list:
        return

    for item in my_list:
        print("{}".format(item))
