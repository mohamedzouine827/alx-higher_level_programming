#!/usr/bin/python3
def uppercase(str):
    the_new_str = ""
    for i in range(len(str)):
        if ord('a') <= ord(str[i]) <= ord('z'):
            the_new_str += chr(ord(str[i]) - 32)
        else:
            the_new_str += str[i]
    print("{}".format(the_new_str))
