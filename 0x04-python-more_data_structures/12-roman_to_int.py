#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_values = {'I': 1, 'V': 5, 'X': 10,
                    'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    reversed_string = roman_string[::-1]
    counter = 0
    prev_value = 0
    for i in range(len(reversed_string)):
        current_value = roman_values[reversed_string[i]]
        if current_value < prev_value:
            counter -= current_value
        else:
            counter += current_value
        prev_value = current_value
    return counter
