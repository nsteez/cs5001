"""
Netti Welsh
Fall 2020 CS5001
Problem 2: recipes
This program will enable users to save and read recipes.
"""

import os
import re
#print statement in main()
#It is OK to split main function to smaller functions
#input validation is required
#repeat the prompt until they get it right


def recipe_to_file(recipe_name):
    recipe_name = recipe_name.lower().strip()
    recipe_name = re.sub("[^A-Za-z0-9 ]", "", recipe_name)
    recipe_name = recipe_name.replace(" ", "_") +".txt"
    return recipe_name

#print(recipe_to_file("   Net%t iSp aghett i8262$    "))

def main():
    #print("MENU: 1 - Save a new recipe, 2 - Read a recipe, 3 - Quit ")
    user_input = 0
    #quit = 3
    valid_input = [1,2,3]

    while user_input != 3:
        try:
            user_input = int(input("MENU: 1 - Save a new recipe, 2 - Read a recipe, 3 - Quit "))
            if user_input == 1:
                print("Saving a New Recipe ")
                #ingredients = input("Enter the ingredients on one line. Separate each ingredient with a comma.").split(",")
                ingredients = []
                while len(ingredients) < 1:
                    valid = False
                    ingredients = input("Enter the ingredients on one line. Separate each ingredient with a comma.").split(",")
                    for i in range(len(ingredients)):
                        ingredients[i] = ingredients[i].strip()
                        if ingredients[i] != "":
                            valid = True
                    if len(ingredients) == 0 or valid == False:
                        print(ingredients)
                        print("Receipe must have at least one ingredient.")
                        ingredients = []
                time = -1
                while time < 0:
                    try:
                        time = int(input("Enter the time needed in minutes: "))
                    except ValueError as ex:
                        time = -1
                    if time < 0:
                        print("Invalid time. Must be an integer greater than or equal to 0.")

                directions = input("(Enter the directions (1 paragraph only): ")
                recipe_name = input("Enter the name of the recipe: ")

                file_name = recipe_to_file(recipe_name)
                while file_name == ".txt":
                    print("Unable to to create the filename.")
                    file_name = input("Enter a string containing only letters, numbers and spaces: ")
                    file_name = recipe_to_file(file_name) # remove spaces, add underscores and .txt at end

                file = open(file_name,'w')
                print(recipe_name, "recipe saved to", file_name)
            elif user_input == 2:
                recipe_name = input("Enter the name of the recipe: ")
                #Attempt to open a file
                #output = open(file,'r') # TODO


            elif user_input == 3:
                break
            else:
                print("Invalid Choice")
        except ValueError as ex:
            print("Enter an Integer")


if __name__ == "__main__":
    main()
