"""
Netti Welsh
CS5001 Fall2020
Problem 2
This program calculates the area of a shape
based on information supplied by the user
"""


def main():
    shapes = ["triangle", "square", "rectangle"]
    u = "Select a shape (triangle, square, or rectangle): "
    user_input = input(u).lower()

    if user_input not in shapes:
        print("Unknown shape")
        return 0

    width = float(input("Enter the width: "))
    if width < 0:
        print("Invalid width")
        return 0
    height = 0
    if user_input != "square":
        height = float(input("Enter the height: "))
    if height < 0:
        print("Invalid height")
        return 0

    if user_input == "triangle":
        triangle = (width * height)/2
        formatted_tri = '{:.2f}'.format(triangle)
        print(f'The area of the triangle is {formatted_tri}')
    elif user_input == "square":
        square = width**2
        formatted_squ = '{:.2f}'.format(square)
        print(f'The area of the square is {formatted_squ}')
    else:
        rectangle = width * height
        formatted_rec = '{:.2f}'.format(rectangle)
        print(f'The area of the rectangle is {formatted_rec}')


if __name__ == "__main__":
    main()
