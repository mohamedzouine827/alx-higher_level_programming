#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            try:
                division_result = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                print("division by 0")
                division_result = 0
            except IndexError:
                print("out of range")
                division_result = 0
                pass
            except TypeError:
                print("wrong type")
                division_result = 0
            new_list.append(division_result)
    finally:
        return new_list
