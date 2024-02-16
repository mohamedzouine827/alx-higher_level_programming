#!/usr/bin/python3
def best_score(a_dictionary):
    Max = 0
    if a_dictionary is not None:
        for i in range(len(a_dictionary)):
            for key, value in a_dictionary.items():
                if value > Max:
                    Max = value
                    max_key = key
            return max_key
    else:
        return None
