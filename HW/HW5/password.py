"""
Netti Welsh
Fall 2020 CS5001
Problem 2: Password
This program checks that a password is valid by taking a string
checking for length of characters. Then checking for three of the following
at least one number, one lowercase, one uppercase or one special character
"""


def secure_password(password):
    ''' Function -- secure_password
                   Checks for password validity
        Paramters: pssword -- takes string input
        Returns -- True -- if length of password is between 9 and 12 chars
                   and contains any three of the following at least
                   one uppercase, at least one lowercase, at least
                   one special char.
                   False -- requirements not met
    '''
    types = 0
    valid_length = len(password) >= 9 and len(password) <= 12
    contains_lower = any(i.islower() for i in password)
    contains_upper = any(i.isupper() for i in password)
    contains_digit = any(i.isdigit() for i in password)
    if valid_length is False:
        return False
    else:
        if invalid_special_chars(password) is True:
            return False
        if contains_lower is True:
            types += 1
        if contains_upper is True:
            types += 1
        if contains_digit is True:
            types += 1
        if valid_special_chars(password) is True:
            types += 1
        return True if types >= 3 else False


def invalid_special_chars(password):
    '''Function -- invalid_special_chars
        This function returns True if password contains an unallowed special
        char
    Parameters:
        password -- string input
    Returns:
        True - if password contains an invalid char, doesnt contain a
        lowercase, uppercase or digit
        False -- otherwise
    '''
    permitted_chars = ['$', '#', '@', '!']
    for i in password:
        if not (i in permitted_chars or i.islower() or i.isupper()
                or i.isdigit()):
            return True
    return False


def valid_special_chars(password):
    '''Function -- valid_special_chars
        This function checks for valid characters by iterating through
        each char in the password and appending them to a used_char list
    Parameters:
        password -- string input
    Returns:
        True - if password contains an valid char,
        False -- otherwise
    '''
    permitted_chars = ['$', '#', '@', '!']
    used_chars = []
    for i in password:
        if i in permitted_chars:
            used_chars.append(i)
    if len(used_chars) == 0:
        return False
    else:
        return True


def main():
    password = input("Enter password: ")
    print(secure_password(password))


if __name__ == "__main__":
    main()
