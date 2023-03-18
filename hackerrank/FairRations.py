#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(B):
    loafs = 0
    odd = [x % 2 for x in B]
    print(odd)
    for i in range(len(odd) - 1):
        print("checking %s is %s" % (i, odd[i]))
        print("%s+1 is %s" % (i, odd[i + 1]))
        if odd[i] == 1:
            print('giving to %s and %s' % (i, i + 1))
            loafs += 2
            odd[i] = 0
            odd[i + 1] = 1 if odd[i + 1] == 0 else 0
    print(odd)

    return str(loafs) if sum(odd) == 0 else "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(result + '\n')

    fptr.close()
