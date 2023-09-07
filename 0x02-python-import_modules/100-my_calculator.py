#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    if len(argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    c = argv[2]

    ops = {"+": add, "-": sub, "*": mul, "/": div}

    if c not in list(ops.keys()):
        print("Unkown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, c, b, ops[c](a, b)))
