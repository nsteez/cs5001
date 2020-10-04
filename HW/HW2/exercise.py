"""
Netti Welsh
CS5001 Fall 2020
Problem 3
This program will create an exercise plan based n the day of
the week and the weather
"""


def main():
    days = ["M", "Tu", "W", "Th", "F", "Sa", "Su"]
    input_day = input("What day is it? ").lower().title()
    is_holiday = input("Is it a holiday? ").capitalize()
    is_raining = input("Is it raining? ").capitalize()
    temperature = float(input("What is the temperature?"))
    y_or_N = ["Y", "N"]
    default = ' Swim for 35 minutes'
    is_workout_day = input_day == "M" or input_day == "W" or \
        input_day == "F" or input_day == "Sa" or is_holiday == "Y"

    if input_day not in days or is_holiday not in y_or_N or \
            is_raining not in y_or_N:
        print(default)
    else:
        if not is_workout_day:
            exercise = "Rest"
        if input_day == 'M' or input_day == 'W' or input_day == 'F':
            exercise = "Run"
        if input_day == 'Sa' or is_holiday == 'Y':
            exercise = "Hike"
        if is_raining == 'Y' and is_workout_day:
            exercise = "Swim"
        duration = 45
        if exercise == "Run" and (temperature > 75 or temperature < 35):
            duration = 30
        if exercise == "Rest":
            print(" Take a rest day")
        else:
            print(f' {exercise} for {duration} minutes')


if __name__ == "__main__":
    main()
