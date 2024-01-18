

packages are way of structuring pythons module namespace by using dotted module names.


cmd arguments
 command utility scripots often need to process command line arguments.tgese arguments are stored in sys modules argv attribute as a list.

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
