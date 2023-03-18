#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def isKaprekar(n):
    len_n = len(str(n))
    sqr_n = n * n
    left_side = int(str(sqr_n)[:-len_n]) if not str(sqr_n)[:-len_n] == "" else 0
    right_side = int(str(sqr_n)[-len_n:]) if not str(sqr_n)[-len_n:] == "" else 0
    if n == (left_side + right_side):
        return str(n)
    else:
        return False


def kaprekarNumbers(p, q):
    res = []
    for x in range(p, q):
        k = isKaprekar(x)
        if not k is False:
            res.append(k)
    print(" ".join(res)) if len(res) > 0 else print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
