"""
Netti Welsh
Fall 2020 CS5001
Problem 2: Hangman

"""
def test(user_guess, word):
    word_list = list(word)
    hidden_word = ""
    for i in word_list:
        if i in user_guess:
            hidden_word += i
        else:
            hidden_word += '_'
    return hidden_word

def check_game_over(hidden_word):
    if "_" in list(hidden_word):
        return False
    else:
         return True

def main():
    words = ["APPLE", "OBVIOUS", "XYLOPHONE"]

    won = 0

    for word in words:
        tries = 6
        user_guess = []

        while tries > 0:
            user_input = input("Enter a letter or word: ").upper()
            if len(user_input) == 1:
                if user_input in user_guess:
                    print("You've already guessed this letter!")
                    continue
                tries -= 1
                user_guess.append(user_input)
                hidden_word = test(user_guess, word)

                print(hidden_word)

                if check_game_over(hidden_word):
                    won += 1
                    print("You won!")
                    break
            else:
                if user_input == word:
                    won += 1
                    print("You win!")
                    break
            print("Your guesses so far: " + " ".join(user_guess))
    print("You won", won, "out of 3")

if __name__ == "__main__":
    main()