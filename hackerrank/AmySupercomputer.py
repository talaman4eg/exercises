#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
from copy import deepcopy


#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#

def dbg_print(*args, **kwargs):
    #print(*args, **kwargs)
    pass

class Plus:
    def __init__(self, cells=[]):
        super().__init__()
        self.cells = cells

    def __str__(self):
        if len(self.cells) > 0:
            return "%s:%s" % (self.cells[0], len(self.cells))
        else:
            return "()"

    def __eq__(self, value):
        return self.square() == value.square()

    def __ne__(self, value):
        return self.square() != value.square()

    def __gt__(self, value):
        return self.square() > value.square()

    def __ge__(self, value):
        return self.square() >= value.square()

    def __lt__(self, value):
        return self.square() < value.square()

    def __le__(self, value):
        return self.square() <= value.square()

    def square(self):
        return len(self.cells)

    def isIntersects(self, that):
        if set(self.cells) & set(that.cells):
            return True
        else:
            return False

    def addCells(self, cells=[]):
        self.cells += cells

    def checkPlus(grid, row, col):
        if grid[row][col] != "G":
            return False
        plus = Plus([(row, col)])
        yield deepcopy(plus)
        lnt = 1
        while True:
            if row - lnt < 0 or grid[row - lnt][col] != "G":
                return
            if row + lnt > len(grid)-1 or grid[row + lnt][col] != "G":
                return
            if col - lnt < 0 or grid[row][col - lnt] != "G":
                return
            if col + lnt > len(grid[0])-1 or grid[row][col + lnt] != "G":
                return
            plus.addCells([(row - lnt, col), (row + lnt, col), (row, col - lnt), (row, col + lnt)])
            yield deepcopy(plus)
            lnt += 1
        # if len(plus.cells) > 1:
        #     dbg_print(plus, plus.cells)
        # return plus

def twoPluses(grid):
    pluses = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            for plus in Plus.checkPlus(grid, row, col):
                heapq.heappush(pluses, (-plus.square(), plus))
            # plus = Plus.checkPlus(grid, row, col)
            # if plus:
            #     heapq.heappush(pluses, (-plus.square(), plus))

    sums = []
    while len(pluses) > 1:
        pl_first = heapq.heappop(pluses)[1]
        pl_copy = pluses.copy()
        pl_next = heapq.heappop(pl_copy)[1]
        while pl_first.isIntersects(pl_next) and len(pl_copy) > 0:
            dbg_print("Intersects", pl_first, pl_next)
            pl_next = heapq.heappop(pl_copy)[1]
        if not pl_first.isIntersects(pl_next):
            dbg_print("Not Intersects", pl_first, pl_next)
            dbg_print(pl_first.cells)
            dbg_print(pl_next.cells)
            heapq.heappush(sums, - (pl_first.square() * pl_next.square()))

    return -heapq.heappop(sums)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
