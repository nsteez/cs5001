"""
Netti Welsh
Fall 2020 CS5001
Problem 2: Hangman
Game that gives players three rounds with 6 tries in each
round to guess a word. Player can enter a word or a single character.
"""


def game_guess(user_guess, word):
    """ Function -- game_guess
            this function converts string input into a list. Creates
            a hidden word of underscores or
             letters based on the list of user_guess
        Parameters:
            user_guess -- a list of user inputs
            word -- word for player to guess
        Returns:
            Combination of underscores and or letters based on user list input
    """
    word_list = list(word)
    hidden_word = ""
    for i in word_list:
        if i in user_guess:
            hidden_word += i
        else:
            hidden_word += '_'
    return hidden_word


def check_game_over(hidden_word):
    """Function -- check_game_over
            checks to see if the game is over by checking if there are any more
            underscores in the word
       Parameters:
            hidden_word -- word player has guessed so far
       Returns: False if underscores remain in the hidden word.
                True if the player guessed hidden letters
                correctly(uncovering the underscores)
    """
    if "_" in list(hidden_word):
        return False
    else:
        return True


def main():
    words = ["APPLE", "OBVIOUS", "XYLOPHONE"]

    won = 0

    for word in words:
        won_round = False
        tries = 6
        user_guess = []
        print("_" * len(word))
        while tries > 0:
            user_input = input("Enter a letter or word: ").upper()
            if len(user_input) == 1:
                if user_input in user_guess:
                    print("You've already guessed that letter!")
                    hidden_word = game_guess(user_guess, word)
                    print(hidden_word)
                    print("Your guesses so far: " + "".join(user_guess))
                    continue
                tries -= 1
                user_guess.append(user_input)
                hidden_word = game_guess(user_guess, word)
                if check_game_over(hidden_word):
                    won += 1
                    print("You won!")
                    break
                else:
                    if tries == 0:
                        print("You lose! The word was", word)
                        break
            else:
                if user_input == word:
                    won += 1
                    print("You win!")
                    break
            hidden_word = game_guess(user_guess, word)
            print(hidden_word)
            print("Your guesses so far: " + "".join(user_guess))
    print("You won", won, "out of 3")


if __name__ == "__main__":
    main()
