#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    score = list(a_dictionary.keys())[0]
    for i in a_dictionary:
        if a_dictionary[score] < a_dictionary[i]:
            score = i
    return score
