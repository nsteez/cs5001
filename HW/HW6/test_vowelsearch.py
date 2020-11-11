from vowelsearch import contains_vowel


def test_contains_vowel():
    assert(contains_vowel(["garage", "this", "man"]) is True)
    assert(contains_vowel(["ffff", "this", "man"]) is False)
    assert(contains_vowel([]) is False)
    assert(contains_vowel(["1.00"]) is False)
    assert(contains_vowel(["&", "45"]) is False)
    assert(contains_vowel(["-1,", "-3"]) is False)
