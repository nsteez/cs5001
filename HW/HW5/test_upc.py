from upc import is_valid_upc, is_valid_upc_split


def test_is_valid_upc_True():
    assert(is_valid_upc('9780128053904') is True)
    assert(is_valid_upc('300819600270') is True)
    assert(is_valid_upc('073854008089') is True)


def test_is_valid_upc_False():
    assert(is_valid_upc('9780128053504') is False)
    assert(is_valid_upc('300819602307') is False)
    assert(is_valid_upc('0738540011089') is False)


def test_is_valid_upc_split():
    assert(is_valid_upc_split('9780128053904') ==
           ([21, 0, 6, 0, 9, 0, 9, 8, 1, 8, 5, 9, 4]))
    assert(is_valid_upc_split('300819600270') ==
           ([0, 24, 27, 0, 6, 0, 3, 0, 1, 6, 0, 7]))
    assert(is_valid_upc_split('073854008089') ==
           ([21, 24, 12, 0, 0, 27, 0, 3, 5, 0, 8, 8]))
