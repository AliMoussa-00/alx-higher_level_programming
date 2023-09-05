#!/usr/bin/python3

def uppercase(str):

    for c in str:
        if ord(c) in range(ord('a'), ord('z') + 1):
            print("{}".format(chr(ord(c) - ord(' '))), end="")
        else:
            print("{}".format(c), end="")
    else:
        print()
