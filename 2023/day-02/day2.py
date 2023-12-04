'''
Advent of Code 2023 - Day 2
Date: 03/12/2023
'''

import logging
import re

############
# PART ONE #
#          #
############

'''
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green


In game 1, three sets of cubes are revealed from the bag (and then put back again). 
The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. 
However, game 3 would have been impossible because at one point the Elf showed you 20 red cubes at once; similarly, 
game 4 would also have been impossible because the Elf showed you 15 blue cubes at once. 
If you add up the IDs of the games that would have been possible, you get 8.
'''


def solve_part1():

    file = open('data.txt', 'r')
    lines = file.read().splitlines()
    
    total = 0
    for line in lines:
        valid_game = True
        game, cubes = line.split(":")
        _, game_id = game.split()

        for subgame in cubes.split(";"):
            for cube in subgame.split(","):
                count, color = cube.split()
                count = int(count)
                if "red" in color and count > 12:
                    valid_game = False
                if "blue" in color and count > 14:
                    valid_game = False
                if "green" in color and count > 13:
                    valid_game = False
        if valid_game:
            total += int(game_id)
        

    #Q: What is the sum of the IDs of those games?
    print("The sum of the IDs of those games: {}".format(total))
    logger.info(f"The sum of the IDs of those games for Q1: {total}")


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
    solve_part2()