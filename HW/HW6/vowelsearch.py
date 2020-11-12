"""
Netti Welsh
Fall 2020 CS5001
Problem 1: vowelsearch
This program takes a list of strings, returns True
if every string in the list contains a vowel
"""

VOWELS = ['a', 'e', 'i', 'o', 'u']


def has_vowels(word, list_vowels):
    """ FUNCTION: has_vowels - checks if a VOWEL is in the word recursively
        PARAMS: word - string in list
                list_vowels - list of VOWELS
        Returns: False - if the length of list_vowels is 0
                 Recursive the first letter in list_value or word and
                 remainder to be checked of list_vowels
    """
    if len(list_vowels) == 0:
        return False
    return list_vowels[0] in word or has_vowels(word, list_vowels[1:])


def contains_vowel(word_lst):
    """FUNCTION:contains_vowel - checks that each word in
                our list of strings contains a vowel
       PARAMS: word_lst - list of strings
       RETURNS: True if there is a vowel in each word in the word_lst
    """
    if len(word_lst) == 0:
        return False
    if len(word_lst) == 1:
        return has_vowels(word_lst[0].lower(), VOWELS)
    return has_vowels(word_lst[0].lower(), VOWELS) and \
        contains_vowel(word_lst[1:])
