#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    length = len(my_list)
    for item in range(length):
        print("{:d}".format(my_list[item]))
