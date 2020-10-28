def factorial_func(n):
    """ original factorial function"""
    a = 1
    while n > 1:
        a = a * n
        n = n-1
    print(a)

def r_factorial_func(n):
    """ recursive factorial """
    if n <=1:
        return 1
    else:
        return n *r_factorial_func(n-1)


def binary_to_decimal():
    """original binary to decimal function """
    binary_num = list(input("Input a binary number: "))
    value = 0
    for i in range(len(binary_num)):
        digit = binary_num.pop()    #an empty pop() will pop out the last value in the list!
        if digit == '1':
            value = value + pow(2, i)
    print(value)


def r_binary_to_decimal(b_num):
    if not b_num:
        return 0
    return binary_to_decimal(b_num[:-1]) * 2 + (b_num[-1])
