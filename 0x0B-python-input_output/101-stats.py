#!/usr/bin/python3
"""Defining the '101-stats' module"""


def print_stats(size, stats):
    """a function that prints our states """

    print(f"File size: {size}")

    for k in sorted(stats):
        print(f"{k}: {stats[k]}")


if __name__ == "__main__":

    from sys import stdin

    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']

    size = 0
    codes = {}
    line_counter = 0

    try:
        for line in stdin:
            if line_counter == 10:
                print_stats(size, codes)
                line_counter = 1
            else:
                line_counter += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                code = line[-2]
                if code in valid_codes:
                    if codes.get(code, -1) == -1:
                        codes[code] = 1
                    else:
                        codes[code] += 1
            except IndexError:
                pass

        print_stats(size, codes)

    except KeyboardInterrupt:
        print_stats(size, codes)
        raise
