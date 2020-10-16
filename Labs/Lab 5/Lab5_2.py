"""
Netti Welsh
Fall 2020 CS5001
Problem 2: binary to decimal
"""

def main():
    binary_num = list(input("Input a binary number: "))
    value = 0
    for i in range(len(binary_num)):
        digit = binary_num.pop()    #an empty pop() will pop out the last value in the list!
        if digit == '1':
            value = value + pow(2, i)
    print(value)

if __name__ == "__main__":
    main()