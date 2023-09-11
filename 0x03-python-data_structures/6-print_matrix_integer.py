#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    if matrix:

        for row in matrix:

            for c in row:
                if c != row[- 1]:
                    print("{}".format(c), end=" ")
                else:
                    print("{}".format(c), end="")
            print()
