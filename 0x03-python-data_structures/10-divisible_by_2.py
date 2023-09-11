#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    if not my_list:
        return my_list

    new_list = my_list.copy()

    for i, num in enumerate(new_list, start=0):

        if int(num) % 2 == 0:
            new_list[i] = True
        else:
            new_list[i] = False

    return new_list
