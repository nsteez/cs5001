"""
Netti Welsh
CS5001 Fall2020 - Lab 11
"""


def r_binary_search(lst, item):
    left_index = 0
    right_index = len(lst) - 1
    middle = (left_index + right_index) // 2
    if len(lst) == 0:
        return False
    if lst[middle] == item:
        return True
    elif item < lst[middle]:
        right_index = middle - 1
    else:
        left_index = middle + 1
    return r_binary_search(lst[left_index:right_index+1], item)


print(r_binary_search([1,3,4,4,7,9,67], 19))
