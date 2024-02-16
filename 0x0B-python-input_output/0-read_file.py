#!/usr/bin/python3
" read file "


def read_file(filename=""):
    "readfile from a txt file"
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
