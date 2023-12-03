'''
Advent of Code 2023 - Day 1
Date: 02/12/2023
'''

import logging

############
# PART ONE #
#          #
############

'''
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are
12, 38, 15, and 77. 

Adding these together produces 142.
'''


def solve_part1():

    file = open('data.txt', 'r')
    lines = file.read().splitlines()

    sum = 0
    total = 0
    # iterate through the list and find the first number
    for line in lines:
        # Loop through the first string 
        for char in line:
            # If first digit is found break the loop
            if (char.isdigit() == True):
                firstDigit = char
                break
        # Loop through the first string in reverse
        for char in line[::-1]:
            # if first digit is found break the loop
            if (char.isdigit() == True):
                lastDigit = char
                break

        sum = int(firstDigit + lastDigit)
        total += sum

    #Q: What is the sum of all of the calibration values?
    print("The sum of all of the calibration values is: {}".format(total))
    logger.info(f"The sum of all of the calibration values for Q1: {total}")

############
# PART TWO #
#          #
############

'''
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
'''
# Replace the strings in the text into numbers we want to get it the same type
# We have to sort the dictionary by longest first so that the replacement doesn't go through in the wrong order starting with the longest string to lowest
# And i'm catching all the edge cases

def solve_part2():

    dict = {
        'one':'o1e',
        'two':'t2o',
        'three':'t3e',
        'four':'f4r',
        'five':'f5e',
        'six':'s6e',
        'seven':'s7n',
        'eight':'e8t',
        'nine':'n9e',
        'zero': 'z0o'

    }


    file = open('data.txt', 'r')
    lines = file.read().splitlines()

    sum = 0
    total = 0
    # iterate through the list and find the first number
    for line in lines:

        # Loop through dictionary and replace string found in the dictionary
        for key, value in dict.items():
            line = line.replace(key, value)

        # Loop through the first string 
        for char in line:
            # If first digit is found break the loop
            if (char.isdigit() == True):
                firstDigit = char
                break
        # Loop through the first string in reverse
        for char in line[::-1]:
            # if first digit is found break the loop
            if (char.isdigit() == True):
                lastDigit = char
                break

        sum = int(firstDigit + lastDigit)
        total += sum

    #Q: What is the sum of all of the calibration values?
    print("The sum of all of the calibration values is: {}".format(total))
    # Use Logger
    logger.info(f"The sum of all of the calibration values for Q2: {total}")




if __name__ == '__main__':
    # Create a basic config
    logging.basicConfig(filemode='w', filename='result.log', level=logging.INFO, format="%(message)s")
    # Create a logger object
    logger = logging.getLogger("--AdventofCode2023--")
    solve_part1()
    solve_part2()