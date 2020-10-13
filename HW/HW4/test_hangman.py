from hangman import game_guess, check_game_over


def test_1():
    assert(game_guess(['A', 'L'], "APPLE") == "A__L_")
    assert(game_guess(['A', 'L', 'E'], "APPLE") == "A__LE")
    assert(game_guess(['T', 'U', 'J', 'X'], "APPLE") == "_____")
    assert(game_guess(['A', 'P', 'L', 'E'], "APPLE") == "APPLE")


def test_2():
    assert(game_guess(['O', 'B'], "OBVIOUS") == "OB__O__")
    assert(game_guess(['O', 'V', 'U'], "OBVIOUS") == "O_V_OU_")
    assert(game_guess(['O', 'B', 'I', 'S', 'V', 'U'], "OBVIOUS") == "OBVIOUS")


def test_3():
    assert(game_guess(['X', 'Y'], "XYLOPHONE") == "XY_______")
    assert(game_guess(['X', 'Y', 'O'], "XYLOPHONE") == "XY_O__O__")


def test_4():
    assert(check_game_over("APPLE") is True)
    assert(check_game_over("OBVIOUS") is True)
    assert(check_game_over("XYOLPHONE") is True)


def test_5():
    assert(check_game_over("_PPL_") is False)
    assert(check_game_over("OBVIOU_") is False)
    assert(check_game_over("X_OLPHON_") is False)
