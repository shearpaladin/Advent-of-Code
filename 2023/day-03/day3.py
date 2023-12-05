'''
Advent of Code 2023 - Day 2
Date: 04/12/2023
'''

import logging
import string

############
# PART ONE #
#          #
############

'''
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 
114 (top right) and 58 (middle right). 
Every other number is adjacent to a symbol and so is a part number; 
their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
'''

'''
-1,-1  0,-1  1, -1
-1,0   0, 0  1, 0
-1,1   0, 1  1, 1
'''

def convert_to_2d_array(pattern):
    """Converts the given multiline string pattern into a 2D array."""
    return [list(row) for row in pattern.split("\n")]

def find_adjacent_elements(arr, x, y):
    """Finds the adjacent elements of the element at position (R, C) in the 2D array."""
    adjacent = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < len(arr) and 0 <= y + j < len(arr[0]) and (i != 0 or j != 0):
                adjacent.append(arr[x + i][y + j])
    return adjacent




def solve_part1():

    file = open('data.txt', 'r')
    lines = file.read()

    engine_schematic = convert_to_2d_array(lines.strip())

    ''' List of symbols except '.' '''
    #[!, ", #, $, %, &, ', (, ), *, +, ,, -, ., /, :, ;, <, =, >, ?, @, [, \, ], ^, _, `, {, |, }, ~]
    symbols= list(string.punctuation)
    symbols.remove(".")

    # Collect all valid parts
    valid_parts = []

    # Get the total number of rows
    total_rows = len(engine_schematic)  


    
    for row_index, row in enumerate(engine_schematic):
        total_columns = len(row) 
        valid = False
        part = ""
        for col_index, char in enumerate(row):
            # Now we have the coordinates (row_index, col_index) for each character
            adjacent_elements = find_adjacent_elements(engine_schematic, row_index, col_index)

            if char.isdigit():
                part+=char

            # Change flag to True if symbol is adjacent to a number
                for element in adjacent_elements:
                    if element in symbols:
                        valid = True
                        
            # Check the last index
                if col_index == total_columns - 1:
                    if part != "":
                        if valid == True:
                            valid_parts.append(int(part))
                            part = ""
                            valid = False

            
            elif (char == ".") or (char in symbols):
                if part != "":
                    if valid == True:
                        valid_parts.append(int(part))
                        part = ""
                        valid = False
                    else:
                        part = ""
            


    #Q: What is the sum of all of the part numbers in the engine schematic?
    print("The sum of the IDs of those games: {}".format(sum(valid_parts)))
    logger.info(f"The sum of the IDs of those games for Q1: {sum(valid_parts)}")




############
# PART TWO #
#          #
############

'''

In game 1, the game could have been played with as few as 4 red, 2 green, and 6 blue cubes. 
If any color had even one fewer cube, the game would have been impossible.
Game 2 could have been played with a minimum of 1 red, 3 green, and 4 blue cubes.
Game 3 must have been played with at least 20 red, 13 green, and 6 blue cubes.
Game 4 required at least 14 red, 3 green, and 15 blue cubes.
Game 5 needed no fewer than 6 red, 3 green, and 2 blue cubes in the bag.
The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together. 
The power of the minimum set of cubes in game 1 is 48. In games 2-5 it was 12, 1560, 630, and 36, respectively.
Adding up these five powers produces the sum 2286.

'''


def solve_part2():
    
    file = open('data.txt', 'r')
    lines = file.read().splitlines()
    
    total = 0
    for line in lines:
        game, cubes = line.split(":")
        _, game_id = game.split()

        cube_count = {
            "blue": 0,
            "red": 0,
            "green": 0
        }

        for subgame in cubes.split(";"):
            for cube in subgame.split(","):
                count, color = cube.split()
                
                if int(count) > int(cube_count[color]):
                    cube_count[color] = int(count)
        
        #print("Game Id {}: {}".format(game_id, cube_count['blue']*cube_count['green']*cube_count['red']) )

        total += cube_count['blue']*cube_count['green']*cube_count['red']


        

    #Q: What is the sum of the IDs of those games?
    print("The sum of the IDs of those games: {}".format(total))
    logger.info(f"The sum of the IDs of those games for Q2: {total}")


if __name__ == '__main__':
    #Create a basic config
    logging.basicConfig(filemode='w', filename='result.log', level=logging.INFO, format="%(message)s")
    # Create a logger object
    logger = logging.getLogger("--AdventofCode2023--")
    solve_part1()
    # solve_part2()