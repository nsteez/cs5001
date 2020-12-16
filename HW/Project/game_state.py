class GameState:
    """
        Class -- GameState
            Represents the checkers board
        Attributes:
            squares -- all the squares on the checker board
            current_player -- current player
            is_game_over -- game over check
    """
    EMPTY = 'EMPTY'
    BLACK = 'BLACK'
    BLACK_KING = 'BLACK_KING'
    RED = 'RED'
    RED_KING = 'RED_KING'

    def __init__(self, squares = None):
        """
            Constructor -- creates instance of GameState
            Parameters:
                self -- the current GameState object
                current_player -- current player(Red or Black)

        """

        if squares == None:
            self.squares = [
                [GameState.EMPTY, GameState.BLACK, GameState.EMPTY, GameState.BLACK, GameState.EMPTY, GameState.BLACK, GameState.EMPTY, GameState.BLACK],
                [GameState.BLACK, GameState.EMPTY, GameState.BLACK, GameState.EMPTY, GameState.BLACK, GameState.EMPTY, GameState.BLACK, GameState.EMPTY],
                [GameState.EMPTY, GameState.BLACK, GameState.EMPTY, GameState.BLACK, GameState.EMPTY, GameState.BLACK, GameState.EMPTY, GameState.BLACK],
                [GameState.EMPTY, GameState.EMPTY, GameState.EMPTY, GameState.EMPTY, GameState.EMPTY, GameState.EMPTY, GameState.EMPTY, GameState.EMPTY],
                [GameState.EMPTY, GameState.EMPTY, GameState.EMPTY, GameState.EMPTY, GameState.EMPTY, GameState.EMPTY, GameState.EMPTY, GameState.EMPTY],
                [GameState.RED,   GameState.EMPTY, GameState.RED,   GameState.EMPTY, GameState.RED,   GameState.EMPTY, GameState.RED,   GameState.EMPTY],
                [GameState.EMPTY, GameState.RED,   GameState.EMPTY, GameState.RED,   GameState.EMPTY, GameState.RED,   GameState.EMPTY, GameState.RED  ],
                [GameState.RED,   GameState.EMPTY, GameState.RED,   GameState.EMPTY, GameState.RED,   GameState.EMPTY, GameState.RED,   GameState.EMPTY],
            ]
        else:
            self.squares = squares
        self.current_player = GameState.BLACK
        self.is_game_over = False
        self.is_testing = False
        self.disable_ai = False
