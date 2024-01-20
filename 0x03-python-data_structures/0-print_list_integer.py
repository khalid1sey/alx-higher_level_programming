#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """A function to print all integers of a list.
    - one integer per line
    - not allowed to import any module
    - assume that list contains integers
    - not allowed to cast integers
    - have to use str.format() to print integers """

    # if not my_list:
    #     return

    # for item in my_list:
    #     print("{}".format(item))
    [print("{}".format(item)) for item in my_list]
