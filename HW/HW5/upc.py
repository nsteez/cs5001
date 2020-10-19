"""
Netti Welsh
Fall 2020 CS5001
Problem 1: Universal product code
This program will take a string as input and return True if
the supplied string is valid
"""

def is_valid_upc(user_input):
    user_input = user_input[::-1]
    if user_input.isdigit() == False:
        return False
    result = is_valid_upc_part2(user_input)
    if sum(result) % 10 ==0:
        return True
    else:
        return False

def is_valid_upc_part2(user_input):
    even_list = []
    odd_list = []
    for i in range(0, len(user_input)):
        user_input_list = list(user_input)
        if i % 2 ==0:
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