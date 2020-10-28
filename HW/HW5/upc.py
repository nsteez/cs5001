"""
Netti Welsh
Fall 2020 CS5001
Problem 1: Universal product code
This program will take a string as input and return True if
the supplied string is a valid universal product code
"""


def is_valid_upc(user_input):
    '''Function --is_valid_upc
        Reverses string input, checks if user_input is a digit,
        checks if the sum of is_valid_upc_part2 is divisible by 10.
    Parameters:
        user_input -- string input
    Returns:
        True -- if sum is divisible by 10
        False -- otherwise
    '''
    user_input = user_input[::-1]
    if user_input.isdigit() is False:
        return False
    result = is_valid_upc_split(user_input)
    if sum(result) % 10 == 0:
        return True
    else:
        return False


def is_valid_upc_split(user_input):
    '''Function -- is_valid_upc_split
        Splits odd and even indexes, multiplies the odd index list integer by 3
        add those values with even indexes integer values
    Parameters:
        user_input -- string input
    Returns:
        The results of the odd index values list combined with
        the even index value list
    '''
    even_list = []
    odd_list = []
    for i in range(0, len(user_input)):
        user_input_list = list(user_input)
        if i % 2 == 0:
            even_list.append(user_input_list[i])
        else:
            odd_list.append(user_input_list[i])
    odd_list_multiplied = [int(i) * 3 for i in odd_list]
    even_list_i = [int(i) for i in even_list]
    return odd_list_multiplied + even_list_i


def main():
    user_input = input("Enter upc")
    print(is_valid_upc(user_input))


if __name__ == "__main__":
    main()
