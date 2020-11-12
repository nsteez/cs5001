"""
Netti Welsh
Fall 2020 CS5001
Problem 2: recipes
This program will enable users to save and read recipes.
"""

import os
import re


def recipe_to_file(recipe_name):
    """FUNCTION: recipe_to_file - converts recipe name to a file name
       PARAMETERS: recipe_name
       RETURNS: filename
    """
    recipe_name = recipe_name.lower().strip()
    recipe_name = re.sub("[^A-Za-z0-9 ]", "", recipe_name)
    recipe_name = recipe_name.replace(" ", "_") + ".txt"
    return recipe_name


def write_file(recipe_name, filename, ingredients, time, directions):
    """FUNCTION: write_file - writes a recipe to a file
       PARAMETERS: recipe_name, filename, ingredients, time, directions
       RETURNS: n/a
    """
    file = open(filename, "w")
    file.write(recipe_name + "\n")
    file.write("\n")
    file.write("Ingredients:\n")
    for ingredient in ingredients:
        file.write(ingredient + "\n")
    file.write("\n")
    file.write("Time: " + str(time) + " minutes\n")
    file.write("\n")
    file.write("Directions:\n")
    file.write(directions)
    file.close()


def validate_ingredients(ingredients):
    """FUNCTION: validate_ingredients - strips white spaces, checks
                 for at least one non-empty ingredient
       PARAMETERS: ingredients - list of strings
       RETURNS: boolean value if ingredients are valid or not
    """
    valid = False
    for i in range(len(ingredients)):
        ingredients[i] = ingredients[i].strip()
        if ingredients[i] != "":
            valid = True
    return valid


def main():
    user_input = 0
    valid_input = [1, 2, 3]
    while user_input != 3:
        try:
            user_input = int(input("MENU: 1 - Save a new recipe, 2 - "
                                   "Read a recipe, 3 - Quit "))
            if user_input == 1:
                ingredients = []
                while len(ingredients) < 1:
                    ingredients = input("Enter the ingredients on one line. "
                                        "Separate each ingredient with a "
                                        "comma. ").split(",")
                    valid = validate_ingredients(ingredients)
                    if len(ingredients) == 0 or valid is False:
                        print("Recipe must have at least one ingredient.")
                        ingredients = []
                directions = input("Enter the directions (1 paragraph only): ")
                time = -1
                while time < 0:
                    try:
                        time = int(input("Enter the time needed in minutes: "))
                    except ValueError as ex:
                        time = -1
                    if time < 0:
                        print("Invalid time. Must be an integer greater "
                              "than or equal to 0.")
                recipe_name = input("Enter a name for the recipe: ")
                file_name = recipe_to_file(recipe_name)
                while file_name == ".txt":
                    print("Unable to create the filename.")
                    file_name = input("Enter a string containing only letters,"
                                      " numbers, and spaces ")
                    file_name = recipe_to_file(file_name)
                write_file(recipe_name, file_name, ingredients,
                           time, directions)
                print(recipe_name, "recipe saved to", file_name)
            elif user_input == 2:
                recipe_name = input("Enter the name of the recipe: ")
                file_name = recipe_to_file(recipe_name)
                try:
                    file = open(file_name, "r")
                    print(file.read())
                except FileNotFoundError:
                    print("Unable to read", file_name)
            elif user_input == 3:
                break
            else:
                print("Invalid choice.")
        except ValueError as ex:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
