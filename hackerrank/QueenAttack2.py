#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def is_on_line(r_q, c_q, r_o, c_o):
    #vertical
    if r_q == r_o:
        return (2, c_o - c_q - 1) if c_o > c_q else (6, c_q - c_o - 1)
    #horiz
    if c_q == c_o:
        return (0, r_o - r_q - 1) if r_o > r_q else (4, r_q - r_o - 1)
    #diag bottom-left to top-right
    if r_q - c_q == r_o - c_o:
        return (1, r_o - r_q - 1) if r_o > r_q else (5, r_q - r_o - 1)
    #diag top-left to bottom-right
    if c_q + r_q == r_o + c_o:
        return (7, r_o - r_q - 1) if r_o > r_q else (3, r_q - r_o - 1)
    return (False, False)


def queensAttack(n, k, r_q, c_q, obstacles):
    moves = [False]*8
    for (r_o, c_o) in obstacles:
        (direction, squares) = is_on_line(r_q, c_q, r_o, c_o)
        if not direction is False:
            if moves[direction] is False or moves[direction] > squares:
                moves[direction] = squares
    #print(n, (r_q, c_q), obstacles, moves)
    #print(moves)
    for direction in range(8):
        if moves[direction] is False:
            if direction == 0:
                moves[direction] = n - r_q
            if direction == 1:
                moves[direction] = min(n - c_q, n - r_q)
            if direction == 2:
                moves[direction] = n - c_q
            if direction == 3:
                moves[direction] = min(n - c_q, r_q - 1)
            if direction == 4:
                moves[direction] = r_q - 1
            if direction == 5:
                moves[direction] = min(r_q - 1, c_q - 1)
            if direction == 6:
                moves[direction] = c_q - 1
            if direction == 7:
                moves[direction] = min(c_q - 1, n - r_q)


    #print(moves)
    return sum(moves)







if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
