#!/usr/bin/python3

for i in range(100):
    print("{:02}{}".format(i, ", " if i < 99 else ""), end="")
else:
    print()
