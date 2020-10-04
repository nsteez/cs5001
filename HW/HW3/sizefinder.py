"""
Netti Welsh
CS5001 Fall 2020
Problem 1
This program is a size finder for a T-shirt company.
User will input measurements and the program will tell them their size
based on our size chart.
"""

def size_chart_kids(chest):
    if 26 <= chest < 28:
        return("S")
    elif 28 <= chest < 30:
        return("M")
    elif 30 <= chest < 32:
        return("L")
    elif 32 <= chest < 34:
        return("XL")
    elif 34 <= chest < 36:
        return("XXL")
    else:
        return("not available")

def size_chart_womens(chest):
    if 30 <= chest < 32:
        return("S")
    elif 32 <= chest < 34:
        return("M")
    elif 34 <= chest < 36:
        return("L")
    elif 36 <= chest < 38:
        return("XL")
    elif 38 <= chest < 40:
        return("XXL")
    elif 40 <= chest < 42:
        return("XXXL")
    else:
        return("not available")


def size_chart_men(chest):
    if 34 <= chest < 37:
        return("S")
    elif 37 <= chest < 40:
        return("M")
    elif 40 <= chest < 43:
        return("L")
    elif 43 <= chest < 47:
        return("XL")
    elif 47 <= chest < 50:
        return("XXL")
    elif 50 <= chest < 53:
        return("XXXL")
    else:
        return("not available")



def main():
    chest = float(input("Chest measurement in inches: "))
    print("Kids size: ", size_chart_kids(chest))
    print("Womens size: ", size_chart_womens(chest))
    print("Mens size: ",size_chart_men(chest))
    print("Sorry, we dont carry your size")


if __name__ == "__main__":
    main()