#!/usr/bin/python3
import sys

arguments = sys.argv[1:]
num_arguments = len(arguments)

if num_arguments != 1:
    print(f"{num_arguments} arguments", end='')
else:
    print(f"{num_arguments} argument", end='')

if num_arguments == 0:
    print('.')
else:
    print(':')
    for i, arg in enumerate(arguments, 1):
        print(f"{i}: {arg}")
