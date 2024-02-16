#!/usr/bin/python3
i = 0
for character in range(122, 96, -1):
    print("{}".format(chr(character - i)), end="")
    if i == 0:
        i = 32
    else:
        i = 0
