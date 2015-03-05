#!/usr/bin/python

# Complete the function below.


def checkUneatenLeaves(N, A):
    eaten = {}            
    for i, a in enumerate(A):        
        to_eat = a
        while to_eat <= N:
            if not to_eat in eaten:
                eaten[to_eat] = 1
            to_eat += a
    uneaten = N - len(eaten)
    return uneaten

def  countUneatenLeaves( N,  A):
    A = sorted(A)
    i = A[0];
    uneaten = i - 1
    while i <= N:
        do_add = True
        for a in A:
            if i % a == 0:
                do_add = False
                break
            if a > i:
                break
        if do_add:
            uneaten += 1
        i += 1

    return uneaten

if __name__ == '__main__':
    N = 8000
    A = [6, 14, 4, 5, 6, 8, 9, 11, 13, 15, 17]

    print countUneatenLeaves(N, A)
    #print checkUneatenLeaves(N, A)