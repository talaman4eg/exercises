#!/usr/bin/python

import copy
import numpy

def float_to_int(fl_num_list, precision = 0.000001):
    for num in range(1, 100000):
        int_num_list = []
        worked = True
        for fl_num in fl_num_list:
            m = fl_num * num
            if abs(round(m) - m) > precision:
                worked = False
                break
            else:
                int_num_list.append(int(round(m)))
        if worked == True:
            int_num_list.append(num)
            break
    return int_num_list





def solution(m):
    """
    >>> solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
    [0, 3, 2, 9, 14]

    >>> solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]])
    [7, 6, 8, 21]

    >>> solution([[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    [0, 0, 0, 0, 0]

    >>> solution([[0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    [1, 1, 0, 0, 2]

    >>> solution([[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [1, 0, 0, 0, 1], [0, 0, 0, 0, 0]])
    [1, 1]

    >>> solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
    [0, 0, 0, 0, 0]

    """

    matrix_size = len(m)
    martix_range = range(0, matrix_size)

    term = []
    non_term = []
    denom = {}

    fl_m = []

    for i in martix_range:
        if max(m[i]) == 0:
            term.append(i)
        else:
            non_term.append(i)
            denom[i] = sum(m[i])

        fl_m.append([])

        row_sum = sum(m[i])
        for j in martix_range:
            fl_m[i].append(0 if row_sum == 0 else float(m[i][j])/float(sum(m[i])))

    if len(non_term) == 1:
        res = m[0]
        if max(res) > 0:
            res.pop(0)
        res_sum = sum(res)
        res.append(res_sum)
        return res
            

    R_m = []
    Q_m = []
    I_min_Q = []
    I_min_Q_den = []

    size_I = len(non_term) 

    I_m = [[1 if i == j else 0 for j in range(size_I)] for i in range(size_I)]

    k = 0
    for i in non_term:
        R_m.append([])
        Q_m.append([])
        for j in non_term:
            Q_m[k].append(fl_m[i][j])
        for j in term:
            R_m[k].append(fl_m[i][j])
        
        k += 1

    I_min_Q = numpy.subtract(I_m, Q_m)

    F_m = numpy.linalg.inv(I_min_Q)
    FR_m = numpy.matmul(F_m, R_m)

    res = float_to_int(FR_m[0])
    return res




    pass

if __name__ == "__main__":
    show_debug = 1
    import doctest
    doctest.testmod()


