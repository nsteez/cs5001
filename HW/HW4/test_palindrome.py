from palindrome import is_palindrome, re


def test_():
    assert(is_palindrome("Madam  Im adam") is True)
    assert(is_palindrome("aa") is True)
    assert(is_palindrome("ra dar") is True)
    assert(is_palindrome("!radar!") is True)


def test_2():
    assert(is_palindrome("a") is False)
    #assert(() == )