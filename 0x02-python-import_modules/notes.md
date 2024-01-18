

packages are way of structuring pythons module namespace by using dotted module names.


cmd arguments

the arguments tht are given after name of program in cmd line shell of os are know as cmd line arguments
 command utility scripts often need to process command line arguments.these arguments are stored in sys modules argv attribute as a list.

----------using sys.argv
the sys module provides functions and variables used to manipulate different parts of python runtime enviroment.
this module provides access to some variables used or maintained by interpreter and functions that interact strongly with the interpreter.

sys.argv is simple list structure its purpose are.
    - lists comd line arguments
    - len(sys.argv) provides the number of cmd line arguments
    - sys.argv[0] is name of the current python script
getopt - is similar to getopt of c function.unlike sys module getopt module extends the separation of the input string by parameter validation.

it allows both short and long options including a calue assignment.its required to remove the forst element from the list of cmd line arguments.

eg #file demo.py
import sys
print(sys.argv)

the argparse module provides a more sophisticated mechanism to process command line arguments.

import argparse

parser = argparse.ArgumentParser(
    prog='top'
    description='Show top lines from eavh file')
parser.add_argument('filenames', nargs='+')
parser.add_argument('-1', '--lines', type+int, default=10)
args = parser.parse_args()
print(args)
