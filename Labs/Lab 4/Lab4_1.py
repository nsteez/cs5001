"""
Netti Welsh
Fall 2020 CS5001
Problem 1: Logarithm
"""
def log(n):
    count = 0
    while n != 1:
        n = n / 2
        count +=1
    print(count)

def main():
    n = int(input("Enter a positive power of 2: "))
    log(n)


if __name__== "__main__":
    main()