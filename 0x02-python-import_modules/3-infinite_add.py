#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    j = 0
    for i, arg in enumerate(argv[1:], start=1):
        j += int(arg)
    print("{}".format(j))
