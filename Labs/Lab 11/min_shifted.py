"""
Netti Welsh
CS5001 Fall2020 - Lab 11
Problem 2: Finding the min in a shifted list
"""

user_input = input()
user_input = user_input.split(',')
lst = [int(num) for num in user_input]
sort = sorted(lst)
print(sort[0])