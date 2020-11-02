from password import secure_password, invalid_special_chars,\
                     valid_special_chars


def test_correct_length_():
    assert(secure_password("123456789") is False)
    assert(secure_password("aaaaaaaaa") is False)
    assert(secure_password("AAAAAAAAAaaa") is False)
    assert(secure_password("bb22bb22bb22") is False)


def test_2_1lower_1upper_1digit():
    assert(secure_password("aaAA1eeee") is True)
    assert(secure_password("AAaaa4yyyyyy") is True)
    assert(secure_password("aaAA1iiigggg") is True)
    assert(secure_password("aaAA1eee11e") is True)


def test_is_valid_password():
    assert(secure_password("aaaaaaaa1#") is True)
    assert(secure_password("AaAAAAaa22!") is True)
    assert(secure_password("!!!!@#$aaaAA") is True)
    assert(secure_password("abCabc!$abc") is True)


def test_invalid_password_with_chars():
    assert(secure_password("aaaaaaaaa#") is False)
    assert(secure_password("aA1aa a a#") is False)
    assert(secure_password("AAAAAAAA!!!") is False)
    assert(secure_password("!!!!@#$aaaaa") is False)
    assert(secure_password("abcabc!$abc") is False)


def test_is_invalid_special_chars():
    assert(invalid_special_chars("Faa,aaaa1,") is True)
    assert(invalid_special_chars("AaA*AAaa22!") is True)
    assert(invalid_special_chars("!!)!@#$aaaAA") is True)
    assert(invalid_special_chars("abC//bc!$abc") is True)
    assert(invalid_special_chars("Faa aaa a1 ") is True)
    assert(invalid_special_chars("abCbc!f!abc") is False)
    assert(invalid_special_chars("abCbc@f@abc") is False)
    assert(invalid_special_chars("abCbc#f#abc") is False)


def test_is_valid_special_chars():
    assert(valid_special_chars("aaaaaaaa1#") is True)
    assert(valid_special_chars("AaAAAAaa22!") is True)
    assert(valid_special_chars("!!!!@#$aaaAA") is True)
    assert(valid_special_chars("abCabc!$abc") is True)
    assert(valid_special_chars("***/aaaAA") is False)
    assert(valid_special_chars("abCabc??abc") is False)
