"""
Netti Welsh
Fall 2020 CS5001
Problem 1: Palidrome
This program takes a string input and returns whether
True or False if it reads the same backwards as it does forward
"""
#import string
import re

def is_palindrome(new_word):
    #reversed_word = ''.join(reversed(word))
    new_word = new_word.replace(' ', '').lower()
    reversed_word = new_word[::-1]
    if len(new_word) < 2:
        return False
    return True if new_word == reversed_word else False

''' if word == reversed_word:
        print(word)
        return True
    else:
        print(word)
        return False
'''




def main():
    #non_letters = "!"
    #usable_letters = ["a","b", "r", "d", "e"]
    #usable_letters = string.ascii_lowercase
    word = input("Enter a word")
    new_word = re.sub("[^a-z]", "", word)

    #print(word)
    #if '!' in word:

    #word = word.replace("!" , '')
    #print(word)

    #for letter in word:

        #print(i)
        #butt = string.ascii_lowercase

      #  if letter not in usable_letters:
      #      letter = letter.replace(letter, ' ')
      #      print(letter)
      #     print(usable_letters)
            #print(butt)
      #      print(word)

    #print(False if len(word) < 2 else is_palindrome(word))
    #if len(word) < 2:
    #    print(False)

    #else:
        #print(is_palindrome(word))
    answer = is_palindrome(new_word)
    print(answer)



if __name__ == "__main__":
    main()