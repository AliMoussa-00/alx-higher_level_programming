def uppercase(str):

    for c in str:
        if ord(c) in range(ord('a'), ord('z') + 1):
            print(f"{chr(ord(c) - ord(' '))}", end="")
        else:
            print(f"{c}", end="")
    else:
        print()
