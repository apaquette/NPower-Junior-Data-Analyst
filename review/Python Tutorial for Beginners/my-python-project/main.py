""" Program that takes user input as a dictionary and 
    converts days into given unit, support hours and minutes.
"""
from helper import validate_and_execute


if __name__ == '__main__':
    while True:
        USER_INPUT = input("Enter a number of days and conversion unit.\n")

        if USER_INPUT.lower() == "exit":
            break

        days_and_unit = USER_INPUT.split(":")
        days_and_unit_dict = {"days": days_and_unit[0], "unit": days_and_unit[1]}
        validate_and_execute(days_and_unit_dict)
