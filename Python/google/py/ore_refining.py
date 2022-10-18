import sys
import math
import copy

show_debug = 0
def dbg(*args):
    if show_debug == 1:
        print(args)

def get_primes():
    return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def denominate(lst):
    """
    >>> denominate([2, 3, 4])
    [2, 3, 4]

    >>> denominate([2, 4, 6])
    [1, 2, 3]

    >>> denominate([6, 12, 18])
    [1, 2, 3]

    """

    primes = get_primes()
    wrk_lst = copy.copy(lst)
    min_val = max(wrk_lst)
    for v in wrk_lst:
        if v != 0 and min_val > v:
            min_val = v
    for prime in primes:
        if prime > min_val:
            break
        divisible = True
        while divisible:
            new_lst = copy.copy(wrk_lst)
            divisible = True
            for i in range(0, len(wrk_lst)):
                if new_lst[i] == 0:
                    continue
                if wrk_lst[i] % prime != 0:
                    divisible = False
                    break
                new_lst[i] /= prime
            if divisible:
                wrk_lst = new_lst
            else:
                break

    return wrk_lst


def least_common_multiple(lst):
    """
    Get least common multiple of the list, ignoting zeros

    >>> least_common_multiple([2, 3, 4])
    12

    >>> least_common_multiple([2, 4])
    4

    >>> least_common_multiple([2, 3, 6])
    6

    >>> least_common_multiple([0, 2, 3, 6])
    6

    """
    primes = get_primes()
    mult = 1
    wrk_lst = copy.copy(lst)
    for v in wrk_lst:
        if v == 0:
            continue
        mult *= v
    for prime in primes:
        if prime >= mult:
            break
        if mult % prime != 0:
            continue
        else:
            while mult % prime == 0:
                divisible = True
                new_mult = mult / prime
                for i in range(0, len(wrk_lst)):
                    if wrk_lst[i] == 0:
                        continue
                    if new_mult % wrk_lst[i] != 0:
                        divisible = False
                        break
                if divisible:
                    mult = new_mult
                else:
                    break
    return mult


def solution(m):
    """
    >>> solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
    [7, 6, 8, 21]

    >>> solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
    [0, 3, 2, 9, 14]

    >>> solution([[0, 1, 1, 0, 0, 1], [4, 0, 0, 3, 2, 0], [2, 0, 0, 2, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
    [0, 3, 2, 9, 14]

    """
    matrix_size = len(m)
    states = [0 for i in range(0, matrix_size+1)]
    non_terminal = []

    wrk_m = copy.deepcopy(m)

    for i in range(0, matrix_size):
        wrk_m[i] = denominate(wrk_m[i])
        states[i] = sum(wrk_m[i])
        if states[i] > 0:
            non_terminal.append(i)



    states[matrix_size] = least_common_multiple(states)

    while non_terminal != [0]:
        for i in non_terminal:
            for j in range(0, matrix_size):
                if wrk_m[i][j] == 0:
                    continue
                if states[j] == 0:
                    continue

                mult = states[i] * states[j]

                val = wrk_m[i][j]
                for k in range(0, matrix_size):
                    if k == i and wrk_m[j][k] != 0:
                        mult -= wrk_m[j][k]
                        wrk_m[i][k] = 0
                        states[i] = mult
                        continue

                    if wrk_m[j][k] == 0:
                        wrk_m[i][k] *= states[j]    
                        
                    wrk_m[i][k] += val * wrk_m[j][k] 

                states[i] = mult
                non_terminal.remove(j)     
    
    res = []
    for i in range(0, matrix_size):
        if states[i] == 0:
            res.append(wrk_m[0][i])

    res.append(states[0])

    return denominate(res)



if __name__ == "__main__":
    show_debug = 1
    import doctest
    doctest.testmod()

    show_debug = 1

    print(solution( [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]] ))
