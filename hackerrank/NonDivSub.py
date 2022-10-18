#!/bin/python3

import math
import os
import random
import re
import sys
import itertools


#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def dbg(*args, **kwargs):
    print(*args, **kwargs)

# bruteforce
def check_num(checked, unchecked, num_index, visited):
    max_len = len(checked)
    if checked in visited:
        dbg("%r already checked" % checked)
        return max_len
    visited.append(checked)
    dbg(checked, unchecked, num_index)
    cur_len = 0
    for candidate in unchecked:
        dbg("Trying candidate = %r" % candidate)
        adding = True
        for c_num in checked:
            dbg("Checking c_num = %r" % c_num)
            if candidate in num_index and c_num in num_index[candidate]:
                dbg("Not adding %r" % candidate)
                adding = False
                break
        if adding:
            dbg("Adding %r" % candidate)
            new_unchecked = list(unchecked)
            new_unchecked.remove(candidate)
            # removing all numbers that are in pair with candidate
            if candidate in num_index:
                for rem in num_index[candidate]:
                    try:
                        new_unchecked.remove(rem)
                    except Exception:
                        pass

            new_checked = sorted(checked + [candidate])
            cur_len = check_num(new_checked, new_unchecked, num_index, visited)
        if max_len < cur_len:
            max_len = cur_len

    return max_len


def nonDivisibleSubset_br(k, s):
    num_index = {}
    # Write your code here
    for num in filter(lambda x, k=k: ((x[1] + x[0]) % k) == 0, itertools.combinations(s, 2)):
        if num[0] in num_index:
            num_index[num[0]].append(num[1])
        else:
            num_index[num[0]] = [num[1]]
        if num[1] in num_index:
            num_index[num[1]].append(num[0])
        else:
            num_index[num[1]] = [num[0]]

    dbg(num_index)
    #exit(1)
    max_len = 1
    visited = []
    for num in s:
        unchecked = list(s)
        unchecked.remove(num)
        cur_len = check_num([num], unchecked, num_index, visited)
        if cur_len > max_len:
            max_len = cur_len

    return max_len

# optimized
def nonDivisibleSubset(k, s):
    #print(k, s)
    remainders = [0]*k
    for x in s:
        remainders[x % k] += 1
    #print(remainders)
    max_len = min(remainders[0], 1)
    for i in range(1, k//2+1):
        if i == k/2 and k % 2 == 0:
            max_len += min(remainders[i], 1)
        else:
            max_len += max(remainders[i], remainders[k-i])

    return max_len


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    fptr.write(str(result) + '\n')

    fptr.close()
