"""
Netti Welsh
Fall 2020 CS5001
Problem 1: Palidrome
This program takes a string input and returns whether
True or False if it reads the same backwards as it does forward
"""

import re


def is_palindrome(new_word):
    """Function -- is_palindrome
            Identifies if the string reads the same backwards
            as it does forward
       Parameters:
            new_word -- input word stripped of non alpha characters
       Returns:
            True if the word is palindrome False otherwise
    """
    new_word = new_word.replace(' ', '').lower()
    reversed_word = new_word[::-1]
    if len(new_word) < 2:
        return False
    return True if new_word == reversed_word else False


def main():
    word = input("Enter a word")
    new_word = re.sub("[^a-z]", "", word)

    answer = is_palindrome(new_word)
    print(answer)


if __name__ == "__main__":
    main()
