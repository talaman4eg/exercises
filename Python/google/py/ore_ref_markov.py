#!/usr/bin/python

import copy

def get_primes():
    return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


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


def substract_rows(row1, den1, row2, den2, mult, mult_den):
    """
    >>> substract_rows([2, 1, 3], 2, [4, 1, 2], 4, 1, 1)
    ([0, 1, 1], 4)
    """
    res = []
    row2_wrk = copy.copy(row2)

    lcm = least_common_multiple([mult_den, den1, den2])
    m2 = lcm/den2
    m1 = lcm/den1
    

    for i in range(len(row2_wrk)):
        #row2_wrk[i] *= m2
        res.append(row1[i]*m1 - row2_wrk[i] * mult)

    lst = denominate(res + [lcm])

    return (lst[:-1], lst[len(lst)-1])




def inverse_matrix(m, denom_list):
    """

    """
    m_wrk = copy.deepcopy(m)
    denom_wrk = copy.deepcopy(denom_list)
    m_size = len(m_wrk)

    inv = [[1 if i == j else 0 for j in range(m_size)] for i in range(m_size)]
    denom_inv = [1 for i in range(m_size)]

    for i in range(m_size):
        # if pivot == 0
        if m_wrk[i][i] == 0:
            for j in range(m_size):
                if j == i or m_wrk[j][i] == 0:
                    continue
                m_wrk[i] = substract_rows(m_wrk[i], denom_wrk[i], m_wrk[j], denom_wrk[i], 1, 1)
                inv[i] = substract_rows(inv[i], denom_inv[i], inv[j], denom_inv[j], 1, 1)
                break
        # zeroing before pivot to make m[i][j] = 0
        for j in range(i):
            mult = m_wrk[i][j]
            mult_den = denom_list[i]
            sub = substract_rows(m_wrk[i], denom_wrk[i], m_wrk[j], denom_wrk[j], mult, mult_den)
            m_wrk[i] = sub[0]
            denom_wrk[i] = sub[1]
            sub = substract_rows(inv[i], denom_inv[i], inv[j], denom_inv[j], mult, mult_den)
            inv[i] = sub[0]
            denom_inv[i] = sub[1]

        # making pivot m[i][i] = 1
        if m_wrk[i][i] != denom_wrk[i]:
            d_w = denom_wrk[i]
            d_i = denom_inv[i]
            denom_wrk[i] *= m_wrk[i][i]
            denom_inv[i] *= inv[i][i]
            for j in range(m_size):
                m_wrk[i][j] *= d_w
                inv[i][j] *= d_i

    for i in range(m_size-2, -1, -1):
        # zeroing after pivot to make m[i][j] = 0
        for j in range(m_size-1, i-1, -1):
            mult = m_wrk[i][j]
            mult_den = denom_list[i]
            sub = substract_rows(m_wrk[i], denom_wrk[i], m_wrk[j], denom_wrk[j], mult, mult_den)
            m_wrk[i] = sub[0]
            denom_wrk[i] = sub[1]
            sub = substract_rows(inv[i], denom_inv[i], inv[j], denom_inv[j], mult, mult_den)
            inv[i] = sub[0]
            denom_inv[i] = sub[1]

    for i in range(m_size):
        v = denominate(m_wrk[i] + [denom_wrk[i]])
        m_wrk[i] = v[:-1]
        denom_wrk[i] = v[len(v) - 1]

        v = denominate(inv[i] + [denom_inv[i]])
        inv[i] = v[:-1]
        denom_inv[i] = v[len(v) - 1]

    return (inv, denom_inv)
    pass


def solution(m):
    """
    >>> solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
    [0, 3, 2, 9, 14]

    >>> solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
    [7, 6, 8, 21]

    """

    matrix_size = len(m)
    martix_range = range(0, matrix_size)

    term = []
    non_term = []
    denom = {}

    for i in martix_range:
        if max(m[i]) == 0:
            term.append(i)
        else:
            non_term.append(i)
            denom[i] = sum(m[i])

        R_m = []
        Q_m = []
        I_min_Q = []
        I_min_Q_den = []

        size_I = len(term) 

        k = 0
        for i in non_term:
            R_m.append(m[i][0:size_I])
            qm = m[i][size_I:]
            Q_m.append(qm)
            imq = []
            j = 0
            for q in qm:
                if k == j: 
                    val = denom[i] - q
                else:
                    val = -q
                imq.append(val)
                j += 1
            I_min_Q.append(imq)
            I_min_Q_den.append(denom[i])

            k += 1

    I_min_Q_inv = inverse_matrix(I_min_Q, I_min_Q_den)




    pass

if __name__ == "__main__":
    show_debug = 1
    import doctest
    doctest.testmod()

    show_debug = 1

    print(solution( [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]] ))
