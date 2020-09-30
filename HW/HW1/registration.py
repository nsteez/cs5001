"""
Netti Welsh
Fall2020 CS5001
This program checks if students can register for courses.
Registration is based on completed prerequisites and on previous course grades.
"""


def main():
    x_courses = ["X101", "X102", ]
    b_courses = ["B500", "B525", "B701"]
    grade_X101 = ["A", "B"]
    grade_X102 = ["A", "B", "C"]
    user_input = input("Enter a course number: ").title().replace(" ", "")

    if user_input not in b_courses and user_input not in x_courses:
        print("Invalid course number")
    elif user_input in x_courses:
        print(f'You have successfully registered for {user_input}')
    elif user_input in b_courses:
        prereq_grade = input("What grade did you get for X101? ").capitalize()
        prereq_grade2 = input("What grade did you get for X102? ").capitalize()
        if prereq_grade in grade_X101 and prereq_grade2 in grade_X102:
            print('You meet all the prerequisites and have',
                  f'successfully registered for {user_input}')
        else:
            print(f'You do not meet the prerequisites for {user_input}')


if __name__ == "__main__":
    main()
