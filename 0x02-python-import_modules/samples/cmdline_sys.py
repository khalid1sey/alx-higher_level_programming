#!/usr/bin/python3
import sys
import getopt

# parser = argparse.ArgumentParser(
#     prog='top',
#     description='Show top lines from eavh file')
# parser.add_argument('filenames', nargs='+')
# parser.add_argument('-1', '--lines', type=int, default=10)
# args = parser.parse_args()
# print(args)
# print(sys.argv)

"""A program that add two numbers and the numbers are passed as cmd line arguments."""

#total arguments
n = len(sys.argv)
print("Total arguments passed: ", n)

#arguments passed
print("\nName of Python script: ", sys.argv[0])

#arguments list
print("\nlist", sys.argv)

#print these list      each in to new line
print("\nArguments Passed: ", end = " ")
for i in range(1, n):
    print(i, ":", sys.argv[i], end = "\n")

#adding them
sum = 0
for j in range(1, n):
    sum += int(sys.argv[j])
print("\n\nResult: ", sum)