movable_spaces_board = [[0, 7], [2, 7], [4, 7], [6, 7],
                        [1, 6], [3, 6], [5, 6], [7, 6],
                        [0, 5], [2, 5], [4, 5], [6, 5],
                        [1, 4], [3, 4], [5, 4], [7, 4],
                        [0, 3], [2, 3], [4, 3], [6, 3],
                        [1, 2], [3, 2], [5, 2], [7, 2],
                        [0, 1], [2, 1], [4, 1], [6, 1],
                        [1, 0], [3, 0], [5, 0], [7, 0]]

class GameState:
    EMPTY = 'EMPTY'
    BLACK = 'BLACK'
    RED = 'RED'
    def __init__(self):
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
        self.current_player = GameState.BLACK

