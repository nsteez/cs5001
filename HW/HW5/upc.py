"""
Netti Welsh
Fall 2020 CS5001
Problem 1:
"""

def is_valid_upc(user_input):
    even_list = []
    odd_list = []
    for i in range(0, len(user_input)):
        user_input_list = list(user_input)
       #print(i)
        if i % 2 ==0:
            even_list.append(user_input_list[i])
        else:
            odd_list.append(user_input_list[i])
    print(even_list)
    print(odd_list)
    odd_list_multiplied = [int(i) * 3 for i in odd_list]
    even_list_i = [int(i) for i in even_list]
    result = odd_list_multiplied + even_list_i
    return sum(result)
    #print(odd_list)


def is_valid_upc2(user_input, result1):
    if is_valid_upc(user_input) % 10 ==0:
        return True
    else:
        return False

def are_integers(user_input):
    return user_input.isdigit()





def main():
    user_input = input("Enter upc ")
    #result = is_valid_upc(user_input)
    #print(result)
    if are_integers(user_input) == True:
        result1 = is_valid_upc(user_input)
        print(is_valid_upc(user_input))
        print(is_valid_upc2(user_input,result1))
    else:
        print(False)



if __name__ == "__main__":
    main()


