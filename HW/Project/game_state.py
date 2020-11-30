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

    def is_game_over(self, BLACK):
        if len(self.squares):
            print("hello")

