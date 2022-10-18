#!/usr/bin/python
import math

def share(received, day, max_days):
    """
    >>> share(5, 1, 5)
    24

    """
    if day > max_days:
        return 0
    shared = int(math.floor(received/2))
    received = shared * 3
    day += 1
    liked = shared
    liked += share(received, day, max_days)
    return liked

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    return share(5, 1, n) 


if __name__ == "__main__":
    import doctest
    doctest.testmod()