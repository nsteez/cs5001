"""
Netti Welsh
Fall2020 CS5001
This program will tell the user how many days there are until Friday
"""

def validation(day):
    '''
     Function: validation
        determines if the users day input is valid
     Parameters:
        day -- input string from user
     Returns
        if the input is in valid_days list. The program returns the number
        of days until friday
    '''
    valid_days = ["M", "Tu", "W", "Th", "F", "Sa","Su"]
    return day in valid_days

def days_from_friday(day):
    '''
     Function: days_from_friday
        returns an output based on day
     Parameters:
        day -- the  day based on users input
     Returns int
    '''
    if day == "M":
        return 4
    elif day ==  "Tu":
        return 3
    elif day == "W":
        return 2
    elif day == "Th":
        return 1
    elif day == "F":
        return 0
    elif day == "Sa":
        return 6
    else:
        return 5


def main():
    user_name = input("What is your name? ")
    print("Hello", user_name)
    current_day = input("What is the current day? M, Tu, W Th F Sa or Su").lower().title()

    if validation(current_day) == True:
        print("The number of days until friday is", days_from_friday(current_day))
    else:
        print("Please enter a valid day")

if __name__ == "__main__":
    main()