"""
Netti Welsh
Fall 2020 CS5001
Problem 2: Hangman

"""

def get_word(round1,round2,round3, guessed, guessed_words):
    if round1 not in guessed_words:
        word = round1
        return word
    if round2 not in guessed_words:
        word = round2
        return word
    elif round3 not in guessed_words:
        word = round3
        return word
    else:
        return "no"

"""
def hidden(word):
    hidden = "-" * len(word)
    return hidden

def game_play(round1, round2, round3):
   pass


def main():
    round1= "APPLE"
    round2 = "OBVIOUS"
    round3 = "XYOLPHONE"
    word = "YES"

    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    #get_word(round1, round2, round3, guessed, guessed_words)
    print(hidden(word))
    #print(hidden(round1, round2, round3))








   # print(hidden_word)
"""

    while not guessed and tries > 0:

        guess = input("Enter a letter or word: ").upper()
        get_word(round1, round2, round3)
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter!")
            elif guess not in word:
                print(guess, "is not in the word")
                tries -=1
                guessed_letters.append(guess)
            else:
                guessed_letters.append(guess)


        elif len(guess) == len(word) and guess.isalpha():
            print("Helllo")
        else:
            print("invalid guess")
        print("Your guesses so far: ", guessed_letters)

"""

if guess in word:
        print("No improvements")
        tries += 1
    elif guess in word_to_guess:
        for i in range(0, len(word_to_guess)):
            if guess == word_to_guess[i]:
                hidden_word_to_guess[i] = guess

"""

if __name__ == "__main__":
    main()