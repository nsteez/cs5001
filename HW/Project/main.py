'''
Netti Welsh
CS 5001, Fall 2020

This code will get you started with the final project, milestone 2.
'''

import math
import turtle
from game_state import GameState


NUM_SQUARES = 8 # The number of squares on each row.
SQUARE = 50 # The size of each square in the checkerboard.
SQUARE_COLORS = ("dim gray", "white")
CIRCLE = 40
BOARD_SIZE = NUM_SQUARES * SQUARE
ORIGIN = [-BOARD_SIZE / 2, -BOARD_SIZE / 2]
board_state = GameState()
clicks = []
SX = 1
SY = 0

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
    sq_y = math.floor((y - ORIGIN[1]) / SQUARE)
    sq_x = math.floor((x - ORIGIN[0]) / SQUARE)
    print(sq_y, sq_x)
    if valid_str == "invalid":
        return
    print(board_state.squares[sq_y][sq_x])
    coordinates = [sq_y, sq_x]
    clicks.append(coordinates)
    if len(clicks) == 1:
        if board_state.squares[sq_y][sq_x] != board_state.current_player:
            print("You can only move your own pieces")
            clicks.clear()
    if len(clicks) == 2:
        make_move(clicks)
        clicks.clear()

# When the move is over, change current player to the other color
def finish_move():
    if board_state.current_player == board_state.BLACK:
        board_state.current_player = board_state.RED
    else:
        board_state.current_player = board_state.BLACK

def make_move(clicks):
    print("Making move", clicks)
    old_location = clicks[0]
    new_location = clicks[1]

    if valid_moves(clicks) is True:
        board_state.squares[old_location[SY]][old_location[SX]] = board_state.EMPTY
        board_state.squares[new_location[SY]][new_location[SX]] = board_state.current_player
        draw_board(turtle.Turtle(), board_state)
        finish_move()

def valid_moves(clicks):
    old_location = clicks[0]
    new_location = clicks[1]

    old_square = board_state.squares[old_location[SY]][old_location[SX]]
    new_square = board_state.squares[new_location[SY]][new_location[SX]]

    if new_square != board_state.EMPTY:
        print("You cannot do capturing moves right now")
        return False

    if old_square == board_state.RED:
        if old_location[SY] - new_location[SY] == 1 and (old_location[SX] - new_location[SX] == -1 or old_location[SX] - new_location[SX] == 1):
            print("Valid red move")
            return True
        else:
            print("Invalid red move")
            return False
    if old_square == board_state.BLACK:
        if old_location[SY] - new_location[SY] == -1 and (old_location[SX] - new_location[SX] == -1 or old_location[SX] - new_location[SX] == 1):
            print("Valid black move")
            return True
        else:
            print("invalid black move")
            return False

def draw_pieces(pen, pieces):
    '''
       Function -- draw_pieces
            draws pieces on the board
       Parameters: pen - pen
                   pieces - list of pieces
                   color - red or black
       Returns: nothing
    '''
    pen.penup() # This allows the pen to be moved.
    pen.hideturtle() # This gets rid of the triangle cursor.
    for row_idx, row in enumerate(pieces):
        for col_idx, col in enumerate(row):
            if pieces[row_idx][col_idx] == GameState.EMPTY:
                continue
            pen.fillcolor(pieces[row_idx][col_idx])
            pen.setposition(ORIGIN[0] + SQUARE / 2 + (col_idx * SQUARE),
                            ORIGIN[0]              + (row_idx * SQUARE))
            draw_circle(pen, SQUARE / 2)


def draw_board(pen, game_state):
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

    draw_pieces(pen, game_state.squares)


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

    draw_board(pen, board_state)

    # Click handling
    screen = turtle.Screen()
    screen.onclick(click_handler) # This will call the click_handler function when a click occurs
    turtle.done() # Stops the window from closing.


if __name__ == "__main__":
    main()
