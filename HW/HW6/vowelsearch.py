"""
Netti Welsh
Fall 2020 CS5001
Problem 1: vowelsearch
This program takes a list of strings, returns True
if every string in the list contains a vowel
"""

VOWELS = ['a','e','i', 'o','u']

def has_vowels(word, list_vowels):
    if len(list_vowels) == 0:
        return False
    return  list_vowels[0] in word or has_vowels(word, list_vowels[1:])


def contains_vowel(word_list):
    if len(word_list) == 0:
        return False
    if len(word_list) == 1:
        return has_vowels(word_list[0].lower(), VOWELS)
    return has_vowels(word_list[0].lower(), VOWELS) and contains_vowel(word_list[1:])

