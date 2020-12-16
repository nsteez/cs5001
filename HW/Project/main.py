'''
Netti Welsh
CS 5001, Fall 2020

Final Project: Checkers Game
This game starts with human user as
player black and computer user as red player
'''

import math
import turtle
from game_state import GameState


NUM_SQUARES = 8
SQUARE = 50
SQUARE_COLORS = ("dim gray", "white")
CIRCLE = 40
BOARD_SIZE = NUM_SQUARES * SQUARE
ORIGIN = [-BOARD_SIZE / 2, -BOARD_SIZE / 2]
SX = 1
SY = 0
DIRECTION_LIST_BLACK = [[1, -1], [1, 1]]
DIRECTION_LIST_KING = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
DIRECTION_LIST_RED = [[-1, 1], [-1, -1]]

board_state = GameState()
clicks = []


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
        radius -- the radius of the circle
    Returns:
        Nothing. Draws a circle in the graphics window.
    '''
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.circle(radius)
    a_turtle.end_fill()
    a_turtle.penup()


def click_handler(x, y):
    '''
        Function -- click_handler
            Called when a click occurs. It checks to see if the click is within
            the board range. It checks two clicks by placing them in the
            coordinates
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
    sq_y = math.floor((y - ORIGIN[1]) / SQUARE)
    sq_x = math.floor((x - ORIGIN[0]) / SQUARE)
    if valid_str == "invalid":
        return
    coordinates = [sq_y, sq_x]
    clicks.append(coordinates)
    if len(clicks) == 1:
        if not is_current_player(board_state, coordinates):
            print("You can only move your own pieces")
            clicks.clear()
        else:
            print(possible_move_all_pieces(board_state))
    if len(clicks) == 2:
        make_move(board_state, clicks)
        clicks.clear()


def switch_player(board_state):
    '''
    Function -- switch_player
        When the move is over, it will change current player to the other color
    Parameters:
        board_state -- current state of the board
    Returns:
        other player

    '''
    other_player = board_state.current_player
    if board_state.current_player == board_state.BLACK:
        board_state.current_player = board_state.RED
    else:
        board_state.current_player = board_state.BLACK
    return other_player


def finish_move(board_state):
    '''
    Function -- finish_move
        When the move is over, it will change current player to
        the other color,then check if the game is over based on
        possible moves
    Parameters:
        board_state - state of the board
    Returns:
        Nothing

    '''

    other_player = switch_player(board_state)
    if len(possible_move_all_pieces(board_state)) == 0:
        print("Game over!", other_player, ' won')
        board_state.is_game_over = True
        return

    move_ai_piece(board_state)


def move_ai_piece(board_state):
    '''
    Function -- move_ai_piece
        checks the possible moves the AI has and selects
        the first possible move in the possible move list. If the
        list of capturing moves is greater than zero. The AI selects the first
        available capturing move.

    Parameters:
        board_state - state of the board
    Returns:
        Nothing

    '''

    if board_state.current_player == board_state.RED and not \
       board_state.disable_ai:
        ai_moves = possible_moves_ai(board_state)
        if len(ai_moves) == 0:
            return
        ai_capturing_moves = filter_capturing_moves_ai(ai_moves)
        ai_move = [[], []]
        if len(ai_capturing_moves) > 0:
            ai_move[0] = ai_capturing_moves[0][0]
            ai_move[1] = ai_capturing_moves[0][1][0]
            ai_move[1][SY] += ai_move[0][SY]
            ai_move[1][SX] += ai_move[0][SX]
        else:
            ai_move[0] = ai_moves[0][0]
            ai_move[1] = ai_moves[0][1][0]
            ai_move[1][SY] += ai_move[0][SY]
            ai_move[1][SX] += ai_move[0][SX]
        make_move(board_state, ai_move)


def make_move(board_state, clicks):
    '''
    Function -- make_move
        Divides two clicks as new location and old
        location to determine where the piece will move on the board.
        The piece moves to the new location if that location is EMPTY
        If there is a capturing move available that move must be made
        before proceeding in the game.

    Parameters:
        board_state - state of the board
        clicks -- a list of clicks formed by click handler
    Returns:
        None

    '''
    if board_state.is_game_over:
        print("Game over, cannot make another move")
        return

    print("Making move", clicks)
    old_location = clicks[0]
    new_location = clicks[1]
    move = [new_location[SY] - old_location[SY], new_location[SX] -
            old_location[SX]]
    moves = possible_move(board_state, old_location)
    capturing_moves = []
    all_moves = possible_move_all_pieces(board_state)
    all_capturing_moves = []

    for move_iterator in moves:
        if move_iterator[SY] % 2 == 0:
            capturing_moves.append(move_iterator)

    for move_iterator in all_moves:
        if move_iterator[SY] % 2 == 0:
            all_capturing_moves.append(move_iterator)
    if len(all_capturing_moves) > 0 and move not in capturing_moves:
        print("You must take a capturing move")
        return

    if move in moves:
        old_piece = board_state.squares[old_location[SY]][old_location[SX]]
        board_state.squares[old_location[SY]][old_location[SX]] \
            = board_state.EMPTY
        if move[SY] % 2 == 0:
            direction = [int(move[SY] / abs(move[SY])),
                         int(move[SX] / abs(move[SX]))]
            current_location = [0, 0]
            current_location[SY] = old_location[SY]
            current_location[SX] = old_location[SX]

            while current_location[SY] \
                != new_location[SY] and current_location[SX] \
                    != new_location[SX]:
                current_location[SY] += direction[SY]
                current_location[SX] += direction[SX]
                board_state.\
                    squares[current_location[SY]][current_location[SX]] \
                    = board_state.EMPTY

        board_state.squares[new_location[SY]][new_location[SX]] = old_piece

        is_king(board_state, clicks)
        if not board_state.is_testing:
            draw_board(turtle.Turtle(), board_state)
        finish_move(board_state)


def possible_move(board_state, location):
    '''
    Function -- possible_move
        checks for possible moves a selected
        piece can make and adds them to a list of possible moves

    Parameters:
        board_state - state of the board
        location -- the coordinates of the the
                    current selected piece
    Returns:
        a list of possible moves for the current piece

    '''
    possible_moves = []
    piece = board_state.squares[location[SY]][location[SX]]

    if piece == board_state.EMPTY:
        return possible_moves

    if piece == board_state.RED:
        possible_direction = DIRECTION_LIST_RED
        opponent_piece = [board_state.BLACK, board_state.BLACK_KING]
    elif piece == board_state.RED_KING:
        possible_direction = DIRECTION_LIST_KING
        opponent_piece = [board_state.BLACK, board_state.BLACK_KING]
    elif piece == board_state.BLACK:
        possible_direction = DIRECTION_LIST_BLACK
        opponent_piece = [board_state.RED, board_state.RED_KING]
    elif piece == board_state.BLACK_KING:
        possible_direction = DIRECTION_LIST_KING
        opponent_piece = [board_state.RED, board_state.RED_KING]

    for direction in possible_direction:
        move_row = location[SY] + direction[SY]
        move_col = location[SX] + direction[SX]
        if move_col < 0 or move_col > 7 or move_row < 0 or move_row > 7:
            continue
        if board_state.squares[move_row][move_col] == board_state.EMPTY:
            possible_moves.append([direction[SY], direction[SX]])
        elif board_state.squares[move_row][move_col] in opponent_piece:
            move_row += direction[SY]
            move_col += direction[SX]
            if move_col < 0 or move_col > 7 or move_row < 0 or move_row > 7:
                continue
            current_move = []
            while board_state.squares[move_row][move_col] == \
                    board_state.EMPTY:
                current_move = [move_row, move_col]
                move_row += direction[SY]
                move_col += direction[SX]
                if not is_inside_board(move_col, move_row):
                    break
                if board_state.squares[move_row][move_col] \
                        not in opponent_piece:
                    break
                move_row += direction[SY]
                move_col += direction[SX]
                if not is_inside_board(move_col, move_row):
                    break
            if len(current_move) > 0:
                possible_moves.insert(0, [current_move[SY] -
                                          location[SY], current_move[SX] -
                                          location[SX]])
    return possible_moves


def possible_move_all_pieces(board_state):
    '''
    Function -- possible_move_all_pieces
           for the current player creates a list of all the possible moves
           available for all the pieces on the board belonging to the
           current player (black or red)

    Parameters:
        board_state - state of the board
    Returns:
        list of all the possible moves for the current player

    '''
    list_of_possible_moves = []

    col = 0
    while col <= 7:
        row = 0

        while row <= 7:
            if is_current_player(board_state, [row, col]):
                possible_move_this_piece = \
                    possible_move(board_state, [row, col])
                if len(possible_move_this_piece) > 0:
                    list_of_possible_moves = list_of_possible_moves + \
                        possible_move_this_piece
            row += 1
        col += 1
    return list_of_possible_moves


def possible_moves_ai(board_state):
    '''
    Function -- possible_moves_ai
        creates a list of all the possble moves for the current player
        in the format expected by our AI

    Parameters:
        board_state - state of the board
    Returns:
        list of all possible moves for the a_i

    '''
    list_of_possible_moves = []

    col = 0
    while col <= 7:
        row = 0

        while row <= 7:
            if is_current_player(board_state, [row, col]):
                possible_move_this_piece = \
                    possible_move(board_state, [row, col])
                if len(possible_move_this_piece) > 0:
                    list_of_possible_moves.append(
                       [[row, col], possible_move_this_piece])
            row += 1
        col += 1
    return list_of_possible_moves


def filter_capturing_moves_ai(list_of_pieces):
    '''
    Function -- filter_capturing_moves_ai
        takes a list of possible moves for the ai and searches to see if
        there is a capturing move available
    Parameters:
        list_of_pieces -- takes a list of possible a_i moves
    Returns:
        a list of possible capturing moves

    '''
    list_of_possible_capturing_moves = []
    for move in list_of_pieces:
        piece_location = move[0]
        piece_possible_moves = move[1]
        piece_possible_capturing_moves = []
        for possible_move in piece_possible_moves:
            if possible_move[SY] % 2 == 0:
                piece_possible_capturing_moves.append(possible_move)
        if len(piece_possible_capturing_moves) > 0:
            list_of_possible_capturing_moves\
                .append([piece_location, piece_possible_capturing_moves])
    return list_of_possible_capturing_moves


def is_inside_board(col, row):
    '''
    Function -- is_inside_board
        checks that x and y coordinates are within range of the board

    Parameters:
        col -- x -coordinates
        row -- y -coordinates
    Returns:
        True or False

    '''
    return False if col < 0 or col > 7 or row < 0 or row > 7 else True


def is_current_player(board_state, location):
    '''
    Function -- is_current_player
       checks if piece at the location belongs to the current player
        player black can move black or black_king pieces
        player red can move red of red_king pieces
    Parameters:
        board_state - state of the board
        location -- location of current piece
    Returns:
        True if the red player clicks on a red piece or red king piece
        True if the black player clicks on a black piece or black king piece
        False otherwise
    '''
    if board_state.current_player == board_state.RED:
        return True if board_state.squares[location[SY]][location[SX]] == \
            board_state.RED or \
            board_state.squares[location[SY]][location[SX]] == \
            board_state.RED_KING else False
    elif board_state.current_player == board_state.BLACK:
        return True if board_state.squares[location[SY]][location[SX]] == \
            board_state.BLACK or \
            board_state.squares[location[SY]][location[SX]] == \
            board_state.BLACK_KING else False
    return False


def is_king(board_state, clicks):
    '''
    Function -- is_king
        checks if black piece land on a black_king spot on the board
        checks if red piece lands on a red_king spot on the board
    Parameters:
        board_state - state of the board
        clicks -- takes the click global variable clicks
    Returns:
        Nothing
    '''
    black_king = [[7, 0], [7, 2], [7, 4], [7, 6]]
    red_king = [[0, 1], [0, 3], [0, 5], [0, 7]]

    if board_state.current_player == 'BLACK':
        if clicks[1] in black_king:
            board_state.squares[clicks[1][SY]][clicks[1][SX]] = \
                board_state.BLACK_KING
    elif board_state.current_player == 'RED':
        if clicks[1] in red_king:
            board_state.squares[clicks[1][SY]][clicks[1][SX]] = \
                board_state.RED_KING


def draw_pieces(pen, pieces):
    '''
       Function -- draw_pieces
            draws pieces on the board
       Parameters: pen - pen
                   pieces - list of pieces
       Returns: nothing
    '''
    pen.penup()

    pen.hideturtle()
    for row_idx, row in enumerate(pieces):
        for col_idx, col in enumerate(row):
            if pieces[row_idx][col_idx] == GameState.EMPTY:
                continue
            color = "WHITE"
            if pieces[row_idx][col_idx] == "RED" or \
                    pieces[row_idx][col_idx] == "RED_KING":
                color = "RED"
            elif pieces[row_idx][col_idx] == "BLACK" or \
                    pieces[row_idx][col_idx] == "BLACK_KING":
                color = "BLACK"
            if pieces[row_idx][col_idx] == "RED_KING" or \
                    pieces[row_idx][col_idx] == "BLACK_KING":
                pen.color("YELLOW", color)
            else:
                pen.color("BLACK", color)
            pen.setposition(ORIGIN[0] + SQUARE / 2 + (col_idx * SQUARE),
                            ORIGIN[0] + (row_idx * SQUARE))
            draw_circle(pen, (SQUARE / 2) - 1)


def draw_board(pen, game_state):
    '''
    Function -- draw_board
    Parameters:
        pen -- pen
        game_state - game_state classs
    Returns:
         Nothing
    '''
    pen.penup()
    pen.hideturtle()
    pen.color("black", "white")
    pen.setposition(ORIGIN[0], ORIGIN[1])
    draw_square(pen, BOARD_SIZE)

    for col in range(NUM_SQUARES):
        for row in range(NUM_SQUARES):
            pen.setposition(ORIGIN[0] + SQUARE * col, ORIGIN[1]
                            + SQUARE * row)
            draw_square(pen, SQUARE)

    pen.color("black", SQUARE_COLORS[0])
    for col in range(NUM_SQUARES):
        for row in range(NUM_SQUARES):
            if col % 2 != row % 2:
                pen.setposition(ORIGIN[0] + SQUARE * col, ORIGIN[1]
                                + SQUARE * row)
                draw_square(pen, SQUARE)

    draw_pieces(pen, game_state.squares)


def main():
    # Create the UI window. The width of the board plus a little margin
    window_size = BOARD_SIZE + SQUARE  # The extra + SQUARE is the margin
    turtle.setup(window_size, window_size)

    # Set the drawing canvas size. The should be actual board size
    turtle.screensize(BOARD_SIZE, BOARD_SIZE)
    turtle.bgcolor("white")  # The window's background color
    turtle.tracer(0, 0)  # makes the drawing appear immediately

    pen = turtle.Turtle()  # This variable does the drawing.
    pen.penup()  # This allows the pen to be moved.
    pen.hideturtle()  # This gets rid of the triangle cursor.

    draw_board(pen, board_state)

    # Click handling
    screen = turtle.Screen()
    screen.onclick(click_handler)  # This will call the click_handler func
    turtle.done()  # Stops the window from closing.


if __name__ == "__main__":
    main()
