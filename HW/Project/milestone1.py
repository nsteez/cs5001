'''
Netti Welsh
CS 5001, Fall 2020

This code will get you started with the final project, milestone 1.
'''

import turtle

NUM_SQUARES = 8 # The number of squares on each row.
SQUARE = 50 # The size of each square in the checkerboard.
SQUARE_COLORS = ("dim gray", "white")
CIRCLE = 40
BOARD_SIZE = NUM_SQUARES * SQUARE
ORIGIN = [-BOARD_SIZE / 2, -BOARD_SIZE / 2]

def draw_square(a_turtle, size):
    '''
        Function -- draw_square
            Draw a square of a given size.
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the length of each side of the square
        Returns:
            Nothing. Draws a square in the graphics window.
    '''
    RIGHT_ANGLE = 90

    a_turtle.begin_fill()
    a_turtle.pendown()
    for i in range(4):
        a_turtle.forward(size)
        a_turtle.left(RIGHT_ANGLE)
    a_turtle.end_fill()
    a_turtle.penup()


def draw_circle(a_turtle, radius):
    '''
    Function -- draw_circle
        Draw a circle with a given radius.
    Parameters:
        a_turtle -- an instance of Turtle
        size -- the radius of the circle
    Returns:
        Nothing. Draws a circle in the graphics windo.
    '''
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.circle(radius)
    a_turtle.end_fill()
    a_turtle.penup()


def click_handler(x, y):
    '''
        Function -- click_handler
            Called when a click occurs.
        Parameters:
            x -- X coordinate of the click. Automatically provided by Turtle.
            y -- Y coordinate of the click. Automatically provided by Turtle.
        Returns:
            Does not and should not return. Click handlers are a special type
            of function automatically called by Turtle. You will not have
            access to anything returned by this function.
    '''
    valid_str = "valid"
    if (x < ORIGIN[0] or x > ORIGIN[0] + BOARD_SIZE):
        valid_str = "invalid"
    if (y < ORIGIN[1] or y > ORIGIN[1] + BOARD_SIZE):
        valid_str = "invalid"
    print("Clicked at ", x, y, "a", valid_str, "position")


def draw_pieces(pen, pieces, color):
    '''
       Function -- draw_pieces
            draws pieces on the board
       Parameters: pen - pen
                   pieces - list of pieces
                   color - red or black
       Returns: nothing
    '''
    pen.fillcolor(color)
    for piece in pieces:
        pen.setposition(ORIGIN[0] + SQUARE / 2 + (piece[0] * SQUARE), ORIGIN[1] + (piece[1] * SQUARE))
        draw_circle(pen, SQUARE / 2)


def main():
    # Create the UI window. This should be the width of the board plus a little margin
    window_size = BOARD_SIZE + SQUARE # The extra + SQUARE is the margin
    turtle.setup(window_size, window_size)

    # Set the drawing canvas size. The should be actual board size
    turtle.screensize(BOARD_SIZE, BOARD_SIZE)
    turtle.bgcolor("white") # The window's background color
    turtle.tracer(0, 0) # makes the drawing appear immediately

    pen = turtle.Turtle() # This variable does the drawing.
    pen.penup() # This allows the pen to be moved.
    pen.hideturtle() # This gets rid of the triangle cursor.

    pen.color("black", "white") # The first parameter is the outline color, the second is the fille

    pen.setposition(ORIGIN[0], ORIGIN[1])
    draw_square(pen, BOARD_SIZE)

    for col in range(NUM_SQUARES):
        for row in range(NUM_SQUARES):
            pen.setposition(ORIGIN[0] + SQUARE * col, ORIGIN[1] + SQUARE * row)
            draw_square(pen, SQUARE)


    pen.color("black", SQUARE_COLORS[0])
    for col in range(NUM_SQUARES):
        for row in range(NUM_SQUARES):
            if col % 2 != row % 2:
                pen.setposition(ORIGIN[0] + SQUARE * col, ORIGIN[1] + SQUARE * row)
                draw_square(pen, SQUARE)

    # 1st number -> how many squares to right from bottom left
    # 2nd number -> how many squares to top from bottom left
    player_red = [[0, 7], [2, 7], [4, 7], [6, 7], [1, 6], [3, 6], [5, 6], [7, 6], [0, 5], [2, 5], [4, 5], [6, 5]]
    player_black = [[1, 0], [3, 0], [5, 0], [7, 0], [0, 1], [2, 1], [4, 1], [6, 1], [1, 2], [3, 2], [5, 2], [7, 2]]

    draw_pieces(pen, player_red, "red")
    draw_pieces(pen, player_black, "black")

    # Click handling
    screen = turtle.Screen()
    screen.onclick(click_handler) # This will call call the click_handler function when a click occurs
    turtle.done() # Stops the window from closing.


if __name__ == "__main__":
    main()
