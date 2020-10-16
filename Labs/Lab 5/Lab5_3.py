"""
Netti Welsh
Fall 2020 CS5001
Problem 3: draw a rectangle
"""

def main():
    width = int(input("Enter width: "))
    height = int(input("Enter height: "))
    char = input("Enter character: ")

    print(char * 6)
    for i in range(height-2):
        print((char + (width-2) * " ") + char)
    print(char * 6)

if __name__ == "__main__":
    main()