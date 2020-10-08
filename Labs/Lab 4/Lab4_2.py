"""
Netti Welsh
Fall 2020 CS5001
Problem 2: Factorial
"""
#import math
def factorial_func(n):
    a = 1
    while n > 1:
        a = a * n
        n = n-1
    print(a)


def main():
    n = int(input("Enter a number: "))
    factorial_func(n)



       #print(math.factorial(n))

if __name__== "__main__":
    main()