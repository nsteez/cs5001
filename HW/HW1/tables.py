"""
Netti Welsh
CS5001 Fall 2020
Problem 2: tables
This program calculates how many tables can be made based off of the
number of parts it's given.
"""


def main():

    tops = int(input("Number of tops: "))
    legs = int(input("Number of legs: "))
    screws = int(input("Number of screws: "))
    tops_per_table = 1
    legs_per_table = 4
    screws_per_table = 8
    top = tops // tops_per_table
    leg = legs // legs_per_table
    screw = screws // screws_per_table

    table_num = min(top, leg, screw)
    l_t = tops - table_num * tops_per_table
    l_l = legs - table_num * legs_per_table
    l_s = screws - table_num * screws_per_table

    print(f'{table_num} tables assembled.'
          f' Leftover parts: {l_t} tops, {l_l} legs, {l_s} screws.')


if __name__ == "__main__":
    main()
