"""
Netti Welsh
CS5001 Fall 2020
Problem 1
This program is a size finder for a T-shirt company.
User will input measurements and the program will tell them their size
based on our size chart.
"""


def size_chart(category, chest_size):
    """ Function -- size_chart
            Identifies which size the user wears
        Parameters:
            category -- The t-shirt company has three sizes Kids Womens
                        and Mens
            chest_size -- The chest size the user inputs in inches
        Returns:
            Size of t-shirt. If chest size is smaller, or larger then the sizes
            we carry then it will return "Not available"

    """
    step = 2
    if category == "M":
        step = 3

    start = 36
    if category == "W":
        start = 42
    elif category == "M":
        start = 53

    if(chest_size >= start):
        return "not available"
    if (category == "W" or category == "M"):
        if chest_size >= (start - step):
            return "XXXL"
        start = start - step
    if((chest_size >= (start - step))):
        return "XXL"
    start = start - step
    if (chest_size >= (start - step)):
        return "XL"
    start = start - step
    if (chest_size >= (start - step)):
        return "L"
    start = start - step
    if (chest_size >= (start - step)):
        return "M"
    start = start - step
    if (chest_size >= (start - step)):
        return "S"
    return "not available"


def results(kids, women, men):
    """Function -- results
           Decides if the comapany has the sizes available
       Parameters:
           kids -- kids t-shirt size or not available string
           women -- womens t-shirt size or not available string
           men -- mens t-shirt size or not available string
       Returns:
           False if the company does not carry size in kids, womens and mens
           else returns True
    """
    if kids == "not available" and women == "not available" \
       and men == "not available":
        return False
    else:
        return True


def main():
    chest_size = float(input("Chest measurement in inches: "))
    kids = size_chart("K", chest_size)
    women = size_chart("W", chest_size)
    men = size_chart("M", chest_size)

    if results(kids, women, men) is False:
        print("Sorry, we don't carry your size")
    else:
        print("Your size choices:")
        print("Kids size: " + kids)
        print("Womens size: " + women)
        print("Mens size: " + men)


if __name__ == "__main__":
    main()
