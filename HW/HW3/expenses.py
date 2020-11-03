"""
Netti Welsh
CS5001 Fall 2020
Problem 2
This program calculates business trip driving expenses
"""


def calculate_mileage(start, end):
    """Function -- calculate_mileage
           Calculates miles driven using the start and end odometer values.
       Parameters:
           start -- The odometer reading at the start of the trip. Expecting a
                    number greater than 0.
           end -- The odometer reading at the end of the trip. Expecting a
                  number greater than 0 and greater than the start value.
       Returns:
           The miles driven, a number. If either parameter is invalid (e.g.
            either parameter is negative or end is less than start), returns 0.
    """
    if start < 0 or end <= 0:
        return 0
    elif end < start:
        return 0
    else:
        mileage = end - start
        return mileage


def get_reimbursement_amount(mileage):
    """Function -- get_reimbursement_amount
           Calculates the amount in dollars that the employee should be
           reimbursed based on their mileage and their mileage and the
           standard rate per mile. The standard rate for 2020 is
           57.5 cents per mile.
       Parameters:
           mileage -- The number of miles driven.
       Returns:
           The amount the employee should be reimbursed in dollars, a float
           round to 2 decimal places.
    """
    standard_rate = 0.575
    amount = mileage * standard_rate
    return round(amount, 2)


def get_actual_mileage_rate(mpg, fuel_price):
    """Function -- get_actual_mileage_rate
            Calculate the actual trip cost per mile in dollars based on the
            car's MPG and the fuel price.
        Parameters:
            mpg -- The car's miles per gallon (MPG), an integer greater than 0.
            fuel_price -- The fuel cost in dollars per gallon, a non-negative
            float.
        Returns:
            The actual cost per miles in dollars, a float rounded to 4 decimal
            places. If supplied arguemnts are invalid, returns 0.0
      """
    mpg = float(mpg)
    if mpg <= 0 or fuel_price <= 0:
        return 0.0
    else:
        cost_per_miles = fuel_price / mpg
        return round(cost_per_miles, 4)


def get_actual_trip_cost(start, end, mpg, fuel_price):
    """Function -- get_actual_trip_cost
           Calculates the cost of a trip in dollars based on the miles driven,
           the MPG of the car, and the fuel price per gallon.
       Parameters:
           start -- The odometer reading at the start of the trip. Expecting a
                    number greater than 0.
            end -- The odometer reading at the end of the trip. Expecting
                   number greater than 0 and greater than the start value.
            mpg -- The car's miles per gallon (MPG), an integer greater than 0.
            fuel_price -- The fuel price per gallon, a non-negative float.
       Returns:
           The cost of the drive in dollars, a float rounded to 2 decimal
           place. If any of the supplied arguements are invalid, returns 0.0
    """

    if mpg <= 0 or fuel_price <= 0 or end <= start:
        return 0.0
    else:
        mileage = calculate_mileage(start, end)
        t_c = (fuel_price / mpg) * mileage
        return round(t_c, 2)


def main():

    print("MILEAGE REIMBURSEMENT CALCULATOR")
    print("Options:")
    print("1 - Calculate reimbursement amount from odometer readings")
    print("2 - Calculate reimbursement amount from miles traveled")
    print("3 - Calculate the actual cost of your trip")
    user_input = int(input("Enter your choice (1, 2, or 3): "))

    r_prompt = "You will be reimbursed $"
    if user_input == 1 or user_input == 3:
        start = int(input("Enter your starting odometer reading: "))
        end = int(input("Enter your ending odometer reading: "))
        if user_input == 3:
            mpg = int(input("Enter your car's MPG: "))
            fuel_price = float(input("Enter the fuel price per gallon: "))
            print("Your trip cost $" +
                  str(get_actual_trip_cost(start, end, mpg, fuel_price)))
        if user_input == 1:
            mileage = calculate_mileage(start, end)
            print(r_prompt +
                  str(get_reimbursement_amount(mileage)))
    elif user_input == 2:
        miles_traveled = int(input("Enter the number of miles traveled: "))
        print(r_prompt +
              str(get_reimbursement_amount(miles_traveled)))

    else:
        print("Not a valid choice")


if __name__ == "__main__":
    main()
