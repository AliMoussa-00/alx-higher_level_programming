#!/usr/bin/python3

def uppercase(str):

    for c in str:
        is_l = ord(c) in range(ord('a'), ord('z') + 1)

        print("{}".format(chr(ord(c) - ord(' ')) if is_l else c), end="")
    else:
        print()
