"""
Netti Welsh
CS5001 Fall 2020
Problem 1: racepace
This program calculates statitics about race time
"""


def main():

    distance_ran = float(input("How many kilometers did you run? "))
    hours = float(input("What was your finish time? Enter hours: "))
    minutes = int(input("Enter minutes: "))

    miles = distance_ran / 1.61

    h_to_s = hours * 3600   # hours to seconds
    m_to_s = minutes * 60   # minute to seconds
    total_seconds = h_to_s + m_to_s  # total amount of seconds
    total_minutes_pace = int(((h_to_s + m_to_s) / 60) / miles)

    total_minutes_to_seconds = total_minutes_pace * 60
    remain_pace = round(((h_to_s + m_to_s) / miles) - total_minutes_to_seconds)
    average_speed = miles / (total_seconds/3600)

    total_time_pace = f'{total_minutes_pace}:{remain_pace}'
    miles_f = '{:.2f}'.format(miles)
    average_speed_f = '{:.2f}'.format(average_speed)
    print(str(miles_f) + " miles, " + str(total_time_pace) +
          " pace, " + str(average_speed_f) + " MPH")


if __name__ == "__main__":
    main()
