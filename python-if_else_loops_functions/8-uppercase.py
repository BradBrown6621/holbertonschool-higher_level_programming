#!/usr/bin/python3
def uppercase(str):
    for i in str:
        c = ord(i)
        offset = 0
        if c in range(97, 123):
            offset = 32
        print("{}".format((chr(c - offset))), end="")
    print("")
