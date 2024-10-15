# Task 1 Leap Year Checker
# Write a Python program that prompts the user to input a year. 
# The program should determine if the given year is a leap year or not and then display an appropriate message.
# Please note that this is the definition of a leap year: 
# Every year that is exactly divisible by four is a leap year,
# except for years that are exactly divisible by 100, but these centurial years are leap years 
# if they are exactly divisible by 400.

# Expected Outcome:
# If you test the year 1900, is should be False. The year 2000 should be True.
# The year 2024 should be True

# NOTE: Ensure that all code in your file is ready to run.
# This means that if someone opens your file and clicks the run button at the top, 
# all code executes as intended. 
# For example, if there are if statements or print statements they should function correctly and display output in the console as expected.

Year = int(input("Enter a year:"))
if (Year % 4 == 0 and Year % 100 != 0) or (Year % 400 == 0):
    print("{} is a leap year".format(Year))
else:
    print("{} is not a leap year".format(Year))