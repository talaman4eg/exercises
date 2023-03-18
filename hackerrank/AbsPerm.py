#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#


def absolutePermutation(n, k):
    init_rng = list(range(1, n + 1))
    res_rng = []
    print(init_rng)
    for i in range(1, n + 1):
        if i - k in init_rng:
            init_rng.remove(i - k)
            res_rng.append(i - k)
            continue
        elif k + i in init_rng:
            init_rng.remove(k + i)
            res_rng.append(k + i)
            continue
        else:
            return [-1]
    return res_rng


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
