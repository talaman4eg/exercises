#!/bin/python3

import math
import os
import random
import re
import sys
import itertools


# https://www.hackerrank.com/challenges/non-divisible-subset/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def checkIfDivisible(k, s):
    if len(s) < 2:
        return False
    for (v1, v2) in itertools.combinations(s, 2):
        if (v1 + v2) % k == 0:
            return True
    return False


def nonDivFinderRecursive(k, s, max_len):
    if len(s) <= max_len:
        return max_len
    print(s)
    print("len(s) = %s, max_len = %s" % (len(s), max_len))
    if len(s) < 2:
        return 0
    is_div = checkIfDivisible(k, s)
    print(is_div)
    if not is_div:
        return len(s)
    if len(s) + 1 == max_len:
        return max_len
    for i in range(len(s)):
        s_copy = s[:]
        print('removing s[%s] = %s:' % (i, s[i]))
        del s_copy[i]
        new_max_len = nonDivFinderRecursive(k, s_copy, max_len)
        if max_len < new_max_len:
            max_len = new_max_len
    return max_len

def nonDivFinderItertools(k, s):
    max_len = 0
    for i in range(2, len(s)):
        combinations = itertools.combinations(s, i)
        found = False
        for comb in combinations:
            print(max_len, i, comb)
            if not checkIfDivisible(k, comb):
                found = True
                max_len = i
                break
        if found == False:
            break
    return max_len


def nonDivFinderQuick(k, s):
    sets = [[]]
    for num in s:
        for i, cur_set in enumerate(sets):
            added = False
            if not checkIfDivisible(k, cur_set + [num]):
                sets[i].append(num)
                added = True
        sets.append([num])
        #print(sets)
    max_len = max([len(cur_set) for cur_set in sets])
    return max_len


def nonDivisibleSubset(k, s):
    max_len = 0
    max_len = nonDivFinderQuick(k, s)
    #max_len = nonDivFinderRecursive(k, s, max_len)
    #max_len = nonDivFinderItertools(k, s)

    return max_len


if name == 'main':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #first_multiple_input = input().rstrip().split()

    n = 87 #int(first_multiple_input[0])

    k = 9 #int(first_multiple_input[1])

    s = [61197933, 56459859, 319018589, 271720536, 358582070, 849720202, 481165658, 675266245, 541667092, 615618805, 129027583, 755570852, 437001718, 86763458, 791564527, 163795318, 981341013, 516958303, 592324531, 611671866, 157795445, 718701842, 773810960, 72800260, 281252802, 404319361, 757224413, 682600363, 606641861, 986674925, 176725535, 256166138, 827035972, 124896145, 37969090, 136814243, 274957936, 980688849, 293456190, 141209943, 346065260, 550594766, 132159011, 491368651, 3772767, 131852400, 633124868, 148168785, 339205816, 705527969, 551343090, 824338597, 241776176, 286091680, 919941899, 728704934, 37548669, 513249437, 888944501, 239457900, 977532594, 140391002, 260004333, 911069927, 586821751, 113740158, 370372870, 97014913, 28011421, 489017248, 492953261, 73530695, 27277034, 570013262, 81306939, 519086053, 993680429, 599609256, 639477062, 677313848, 950497430, 672417749, 266140123, 601572332, 273157042, 777834449, 123586826] #list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    print(result)