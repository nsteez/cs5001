from main import possible_move, switch_player, finish_move,\
        possible_move_all_pieces, possible_moves_ai, \
        make_move, \
        filter_capturing_moves_ai, \
        is_inside_board, is_current_player


from game_state import GameState
g = GameState()


def test_possible_move():
    game = GameState()
    assert(possible_move(game, [2, 1]) == [[1, -1], [1, 1]])
    assert(possible_move(game, [0, 2]) == [])

    game2 = GameState([
     [g.EMPTY, g.BLACK, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.RED,   g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.BLACK_KING, g.EMPTY, g.EMPTY, g.EMPTY,
      g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
    ])
    assert(game2.current_player == game2.BLACK)
    assert(possible_move(game2, [2, 1]) == [
        [-2, 2], [-1, -1], [1, -1], [1, 1]]
    )

    game3 = GameState([
     [g.EMPTY, g.BLACK, g.EMPTY, g.EMPTY, g.EMPTY, g.BLACK, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.BLACK, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.RED, g.EMPTY, g.BLACK, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     ])
    assert(game3.current_player == game3.BLACK)
    assert(possible_move(game3, [0, 5]) == [[1, -1], [1, 1]])


def test_switch_player():
    game = GameState()
    assert(game.current_player == game.BLACK)
    assert(switch_player(game) == game.BLACK)
    assert(game.current_player == game.RED)
    assert(switch_player(game) == game.RED)
    assert(game.current_player == game.BLACK)


def test_possible_move_all_pieces():
    game1 = GameState()
    assert(len(possible_move_all_pieces(game1)) > 0)

    # Black player has no moves, therefore should return an empty list
    game2 = GameState([
     [g.EMPTY, g.BLACK, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.RED,   g.EMPTY, g.RED,   g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.RED,   g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
    ])
    assert(game2.current_player == game2.BLACK)
    assert(len(possible_move_all_pieces(game2)) == 0)
    # Black has 8 possible moves should return 8
    game3 = GameState([
     [g.EMPTY, g.BLACK, g.EMPTY, g.EMPTY, g.EMPTY, g.BLACK, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.BLACK, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.RED, g.EMPTY, g.BLACK, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     ])
    assert(game3.current_player == game3.BLACK)
    assert(len(possible_move_all_pieces(game3)) == 8)

    game4 = GameState([
     [g.EMPTY, g.BLACK, g.EMPTY, g.EMPTY, g.EMPTY, g.BLACK, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.BLACK, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.RED, g.EMPTY, g.RED, g.EMPTY, g.BLACK, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.BLACK, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.BLACK_KING, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY,
      g.EMPTY, g.EMPTY, g.EMPTY],
     ])
    assert(game4.current_player == game4.BLACK)
    assert(len(possible_move_all_pieces(game4)) == 11)


def test_possible_moves_ai():
    game1 = GameState()
    game1.current_player = game1.RED
    assert(len(possible_moves_ai(game1)) > 0)

    game2 = GameState([
     [g.EMPTY, g.BLACK, g.EMPTY, g.BLACK, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.RED,   g.EMPTY, g.RED,   g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
    ])
    game2.current_player = game2.RED
    assert(game2.current_player == game2.RED)
    assert(len(possible_move_all_pieces(game2)) == 0)

    game3 = GameState([
     [g.EMPTY, g.BLACK, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.RED,   g.EMPTY, g.RED,   g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
    ])
    game3.current_player = game3.RED
    assert(game3.current_player == game3.RED)
    assert(len(possible_move_all_pieces(game3)) == 1)


def test_filter_capturing_moves_ai():
    assert((filter_capturing_moves_ai([
        [[5, 0], [[-1, 1]]],
        [[5, 2], [[-1, 1], [-1, -1]]],
        [[5, 4], [[-1, 1], [-1, -1]]],
        [[5, 6], [[-1, 1], [-1, -1]]]])) == []
    )
    assert(filter_capturing_moves_ai([
        [[5, 0], [[-2, 2]]],
        [[5, 2], [[-1, 1], [-1, -1]]]]) == [[[5, 0], [[-2, 2]]]]
    )


def test_is_inside_board():
    assert(is_inside_board(0, 2) is True)
    assert(is_inside_board(0, 8) is False)


def test_is_current_player():
    game = GameState()
    assert(game.current_player == game.BLACK)
    assert(is_current_player(game, [0, 1]) is True)
    assert(is_current_player(game, [5, 0]) is False)


def test_make_move():
    game = GameState([
     [g.EMPTY, g.BLACK, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.RED,   g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.BLACK_KING, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY,
         g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.RED, g.EMPTY,   g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
    ])
    game.is_testing = True
    game.disable_ai = True
    assert(game.current_player == game.BLACK)

    make_move(game, [[2, 1], [0, 3]])

    assert(game.current_player == game.RED)
    assert(game.squares[2][1] == game.EMPTY)
    assert(game.squares[1][2] == game.EMPTY)
    assert(game.squares[0][3] == game.BLACK_KING)

    game2 = GameState([
     [g.EMPTY, g.BLACK, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY,   g.EMPTY, g.RED, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.BLACK_KING, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY,
         g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY,   g.RED, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
     [g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY, g.EMPTY],
    ])
    game2.is_testing = True
    game2.disable_ai = True
    assert(game2.current_player == game2.BLACK)

    make_move(game2, [[0, 1], [1, 2]])

    assert(game2.current_player == game2.RED)
    assert(game2.squares[1][2] == game2.BLACK)
    assert(game2.squares[1][0] == game2.EMPTY)
