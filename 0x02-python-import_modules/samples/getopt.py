import getopt, sys

"""A program to demonstrate cmd line arguments with help oh getopt module"""

#remove first argument from list
argList = sys.argv[1:]

#options
options = "hmo:"

#long options
long_options = ["Help", "My_file", "Output="]

 