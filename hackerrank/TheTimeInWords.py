#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    """
    >>> timeInWords(5, 0)
    "five o' clock"
    >>> timeInWords(5, 1)
    'one minute past five'
    >>> timeInWords(5, 10)
    'ten minutes past five'
    >>> timeInWords(5, 15)
    'quarter past five'
    >>> timeInWords(5, 30)
    'half past five'
    >>> timeInWords(5, 40)
    'twenty minutes to six'
    >>> timeInWords(5, 45)
    'quarter to six'
    >>> timeInWords(5, 47)
    'thirteen minutes to six'
    >>> timeInWords(5, 28)
    'twenty eight minutes past five'
    >>> timeInWords(5, 21)
    'twenty one minutes past five'


    """
    teens = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
        8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
        14: "forteen",
        # skipping 15
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
    }

    if int(m) == 0:
        res = teens[h] + " o' clock"
        return res
    else:
        res = ""
        if m < 31:
            suffix = " past "
        else:
            suffix = " to "
            m = 60 - m
            h += 1
            if h > 12:
                h = 1
        units = " minutes"
        if m == 15:
            res = "quarter"
            units = ""
        if m == 30:
            res = "half"
            units = ""
        if m in teens:
            res = teens[m]
        if m == 1:
            units = " minute"


        if m > 19 and m < 30:
            res = "twenty"
            m -= 20
            if m in teens:
                res += " " + teens[m]
        res += units + suffix + teens[h]
    return res


if __name__ == '__main__':

    if len(sys.argv) > 1 and sys.argv[1] == "test":
        import doctest
        doctest.testmod()
        quit()


    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
