"""
Name: Hongyu Guo
Course: CMPSC 132
File: Grade.py
Date: September 4, 2024
Short description: Functions for calculate the average and grade converter
"""

# Function for calculate average of the total score
def calc_average(list_input):

    # Identify how many items inside list
    grades = len(list_input)
    # Calculation for total sum of the list
    grade_sum = sum(list_input)

    # Calculation for average of total score
    grade_avg = grade_sum/grades
    return grade_avg

# Function for number grade to letter grade convertion
def grade_converter(grade_input):
    # Verifies it is a valid grade (0~100) first
    if (grade_input < 0) or (grade_input > 100):
        print('Invalid score.')
        return
    elif grade_input < 60:
        return 'F'
    elif grade_input < 70:
        return 'D'
    elif grade_input < 80:
        return 'C'
    elif grade_input < 90:
        return 'B'
    else:
        return 'A'
