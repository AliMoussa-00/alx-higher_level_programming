#!/usr/bin/python3
"""Defining the '101-stats' module"""


def print_stats(size, stats):
    """a function that prints our states """

    print(f"File size: {size}")

    for k, v in sorted(stats.items()):
        print(f"{k}: {v}")


if __name__ == "__main__":

    from sys import stdin

    codes = ['200', '301', '400', '401', '403', '404', '405', '500']

    states = {}
    file_size = 0
    line_counter = 0

    try:

        for line in stdin:

            line_counter += 1
            if line_counter == 10:

                print_stats(size, states)
                line_counter = 1

            else:
                line_counter += 1

            data = line.split()

            try:
                file_size += int(data[-1])
            except (IndexError, ValueError):
                pass

            try:
                code = data[-2]

                if code in codes:

                    if states.get(code, -1) == -1:

                        states[code] = 1

                    else:
                        states[code] += 1

            except IndexError:
                pass

            print_stats(file_size, states)

    except KeyboardInterrupt:
        print_stats(file_size, states)
        raise
