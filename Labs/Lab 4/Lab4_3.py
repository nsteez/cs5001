"""
Netti Welsh
Fall 2020 CS5001
Problem 3: Calculator
"""


def calc(num):
    pass


def subtract(num, arthimetic_op):
    num2 = float(arthimetic_op[1:])
    total = num- num2
    return total


def add(num, arthimetic_op):
    num2 = float(arthimetic_op[1:])
    total = num + num2
    return total


def multiply(num, arthimetic_op):
    num2 = float(arthimetic_op[1:])
    total = num * num2
    return total


def divide(num, arthimetic_op):
    num2 = float(arthimetic_op[1:])
    total = num / num2
    return total

def main():
    num = float(input("Enter a number "))
    total = num
    while num != "q" and num != "Q":
        arthimetic_op = input("Enter the next step in the calculation: ")
        index_1 = arthimetic_op[:1]
        if index_1 == "*":
            multiplication = multiply(num, arthimetic_op)
            #print(multiplication)
            total *= float(arthimetic_op[1:])
            print(total)
        elif index_1 == "/":
            division = divide(num, arthimetic_op)
            total /= float(arthimetic_op[1:])
            print(total)
            #print(division)
        elif index_1 == "+":
            addition = add(num, arthimetic_op)
            total += float(arthimetic_op[1:])
            print(total)
        elif index_1 == "-":
            subtraction = subtract(num, arthimetic_op)
            total -= float(arthimetic_op[1:])
            print(total)
            #print(subtraction)
        else:
            print("Total = " + str(total))
            break




if __name__== "__main__":
    main()