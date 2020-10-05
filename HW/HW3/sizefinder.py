"""
Netti Welsh
CS5001 Fall 2020
Problem 1
This program is a size finder for a T-shirt company.
User will input measurements and the program will tell them their size
based on our size chart.
"""

def size_chart(category, chest_size):
    step = 2
    if category == "M":
        step = 3

    start = 36
    if category == "W":
        start = 42
    elif category == "M":
        start = 53

    if(chest_size > start):
        return "Not available"
    if (category == "W" or category == "M"):
        if chest_size >= (start- step):
            return "XXXL"
        start = start - step
    if((chest_size >= (start - step))):
        return "XXL"
    start = start- step
    if (chest_size >= (start-step)):
        return "XL"
    start = start- step
    if (chest_size >= (start-step)):
        return "L"
    start = start - step
    if (chest_size >= (start-step)):
        return "M"
    start = start - step
    if (chest_size >= (start-step)):
        return "S"
    start = start - step
    if (chest_size >= (start-step)):
        return "Not available"



def main():
    chest_size = float(input("Chest measurement in inches: "))
    size_chart("K", chest_size)
    size_chart("W", chest_size)
    size_chart("M", chest_size)

    if size_chart("K",chest_size)== "Not available" and \
        size_chart("W", chest_size) == "Not available" and \
        size_chart("M",chest_size) == "Not available":
        print("Sorry, we dont carry your size")
    else:
        print("Kids size: ", size_chart("K", chest_size))
        print("Womens size: ", size_chart("W", chest_size))
        print("Mens size: ",size_chart("M",chest_size))

if __name__ == "__main__":
    main()