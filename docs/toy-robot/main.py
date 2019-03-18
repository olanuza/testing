#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re


# Map configuration
X_MAX_LENGTH = 5
Y_MAX_LENGTH = 5
place_format = re.compile(r"[0-%i],[0-%i],\b(NORTH|EAST|SOUTH|WEST)\b" % (X_MAX_LENGTH - 1,
                                                                          Y_MAX_LENGTH - 1))


def get_valid_commands(commands):
    """
    Return a valid set of commands for the robot.

    >>> get_valid_commands(['PLACE', '0,0,EAST', 'MOVE'])
    ['PLACE', '0,0,EAST', 'MOVE']

    >>> get_valid_commands(['REPORT', 'MOVE', 'PLACE', '0,0,EAST', 'MOVE'])
    ['PLACE', '0,0,EAST', 'MOVE']

    >>> get_valid_commands(['PLACE', '0,0,EASTO', 'MOVE'])
    []

    >>> get_valid_commands(['PLACE', '0,0,EASTO', 'MOVE', 'PLACE', '1,3,NORTH', 'REPORT'])
    ['PLACE', '1,3,NORTH', 'REPORT']
    """
    for i in range(0, len(commands)):
        if commands[i] == 'PLACE' and place_format.match(commands[i+1]):
            return commands[i:]

    return []


def execute_commands(commands):
    """
    Move the robot as defined by the rules.

    >>> execute_commands(['PLACE', '0,0,NORTH', 'MOVE', 'REPORT'])
    0,1,NORTH

    >>> execute_commands(['PLACE', '0,0,NORTH', 'LEFT', 'REPORT'])
    0,0,WEST

    >>> execute_commands(['PLACE', '1,2,EAST', 'MOVE', 'MOVE', 'LEFT', 'MOVE', 'REPORT'])
    3,3,NORTH
    """
    robot = {'X': None, 'Y': None, 'direction': None}
    moves = {'NORTH': [0, 1], 'EAST': [1, 0], 'SOUTH': [0, -1], 'WEST': [-1, 0]}
    directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']

    for i in range(0, len(commands)):
        command = commands[i]
        
        if command == 'PLACE':
            if place_format.match(commands[i+1]):
                X, Y, DIR = commands[i+1].split(',')
                
                robot['X'] = int(X)
                robot['Y'] = int(Y)
                robot['direction'] = DIR
                
        elif command == 'MOVE':
            delta_X, delta_Y = moves[robot['direction']]
            new_X = robot['X'] + delta_X
            new_Y = robot['Y'] + delta_Y

            if new_X < X_MAX_LENGTH and new_Y < Y_MAX_LENGTH:
                robot['X'] = new_X
                robot['Y'] = new_Y
            
        elif command == 'LEFT':
            new_dir = directions[(directions.index(robot['direction']) - 1) % 4]
            robot['direction'] = new_dir
            
        elif command == 'RIGHT':
            new_dir = directions[(directions.index(robot['direction']) + 1) % 4]
            robot['direction'] = new_dir
            
        elif command == 'REPORT':
            print("%i,%i,%s" % (robot['X'], robot['Y'], robot['direction']))
        
    return None


if __name__ == '__main__':
    commands = get_valid_commands(sys.argv[1:])
    execute_commands(commands)
    
