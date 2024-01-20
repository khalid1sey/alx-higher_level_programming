#!/usr/bin/python3
"""A program to print all integers of a list.
    - one integer per line
    - not allowed to import any module
    - assume that list contains integers
    - not allowed to cast integers
    - have to use str.format() to print integers """


def print_list_integer(my_list=[]):

    for item in my_list:
        print("{}".format(item))
