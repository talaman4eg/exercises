#!/usr/bin/python

import sys

show_debug = 0

def dbg(*args):
    if show_debug == 1:
        print(args)

def substract(x, y, base):
    #dbg(x,y, base)
    x = list(x)
    y = list(y)
    if len(x) > len(y):
        y = y.zfill(len(x))
    if len(x) < len(y):
        x = x.zfill(len(y))

    z = list('0'.zfill(len(x)))

    for i in range(len(x)-1, -1, -1):
        #dbg('iter', i)
        sub = int(x[i]) - int(y[i])
        #dbg('sub', sub)

        if sub >= 0:
            z[i] = str(sub)
        else:
            z[i] = str(base - abs(sub))
            #dbg("z[%s] = %s" % (i, z[i]))
            j = i - 1
            while x[j] == 0 and j >= 0:
                j -= 1
            x[j] = str(int(x[j]) - 1)

    return z



def solution(n, b):
    #Your code here
    ids = [n]
    iter = 0
    while iter < 10:
        n = list(n)
        iter += 1
        num1 = sorted(n)
        num2= sorted(n, reverse=True)
        next = substract(num2, num1, b)
        str_next = ''.join(next)
        dbg(n, next, str_next, num2, num1, iter)
        if str_next in ids:
            return len(ids) - ids.index(str_next)
        ids.append(str_next)
        n = next

if __name__ == '__main__':
    show_debug = 1

    #print(substract(sys.argv[1], sys.argv[2], int(sys.argv[3])))

    print(solution(sys.argv[1], int(sys.argv[2])))
    print('\n')
