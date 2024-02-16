#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, div, sub, mul
    from sys import argv as my_args
    import sys
    lenght = len(my_args)
    if (lenght - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        operator = my_args[2]
        arg_1 = int(my_args[1])
        arg_2 = int(my_args[3])
        if operator == '+':
            print("{} + {} = {}".format(arg_1, arg_2, add(arg_1, arg_2)))
        elif operator == '*':
            print("{} * {} = {}".format(arg_1, arg_2, mul(arg_1, arg_2)))
        elif operator == '-':
            print("{} - {} = {}".format(arg_1, arg_2, sub(arg_1, arg_2)))
        elif operator == '/':
            print("{} / {} = {}".format(arg_1, arg_2, div(arg_1, arg_2)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
