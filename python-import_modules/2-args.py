#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    length = (len(sys.argv) - 1)
    print("{} argument".format(length), end="")
    if length == 0 or length > 1:
        print("s", end="")
    print(":")
    if length > 0:
        for i in range(1, length + 1):
            print("{}: {}".format(i, sys.argv[i]))
