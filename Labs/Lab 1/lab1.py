'''
Netti Welsh
Fall2020
CS 5001
Problem 1 - Eating out with a group
Calculating the price per person splitting the bill
'''
def main():

    amount = float(input("How much was the bill?"))
    tip = float(input("Enter tip amount ")) 
    people = int(input("Enter the amount of people "))


    total = ((amount * tip) + amount) / people

    print(total)

if __name__ == "__main__":
    main()    

