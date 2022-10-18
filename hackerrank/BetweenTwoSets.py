#!/usr/bin/python3

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    maxA = max(a)
    minB = min(b)

    candidates = [maxA, minB]

    print(a, b)

    for i in range(maxA, int(minB/2)+1):
        if minB % i == 0:
            candidates.append(i)



    print(a, b)
    res = []
    print( candidates)
    for cand in candidates:
        doAdd = True
        for i in a:
            if cand % i != 0:
                doAdd = False
                break
        if doAdd == False:
            continue

        for j in b:
            if j % cand != 0:
                doAdd = False
                break
        if doAdd and not cand in res:
            res.append(cand)

    print (res)
    return len(res)

if __name__ == '__main__':

    arr = list(map(int, "3 9 6".rstrip().split()))

    brr = list(map(int, "36 72".rstrip().split()))

    total = getTotalX(arr, brr)

    print(str(total) + '\n')
