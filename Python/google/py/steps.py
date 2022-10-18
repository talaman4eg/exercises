import sys
import math
show_debug = 0
def dbg(*args):
    if show_debug == 1:
        print(args)

cache = {}

def max_first(n):
    """
    >>> max_first(10)
    4
    >>> max_first(11)
    5
    """
    first = int(math.ceil(((-1 + math.sqrt(1 + 8 * n))/2)))
    return first

def process_recursive(current, left):
    """
    >>> process_recursive(1, 0)
    1
    >>> process_recursive(5, 3)
    2
    >>> process_recursive(6, 5)
    3
    """
    if left < 3:
        return 1
    cache_key = "%s_%s" % (current, left)
    if cache_key in cache.keys():
        return cache[cache_key]
    variants = 0
    dbg("current", current, 'left', left)
    r = range(left if left < current else current - 1, max_first(left)-1, -1)
    dbg(r)
    for i in r:
        variants += process_recursive(i, left-i)

    dbg("current", current, 'left', left, 'variants', variants)
    cache[cache_key] = variants
    return variants



def solution(n):
    variants = 0
    first = max_first(n)
    dbg('first', first)
    for i in range(first, n):
        dbg("sol current", i, 'left', n-i)
        variants += process_recursive(i, n-i)

    return variants


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    show_debug = 0
    print(solution(int(sys.argv[1])))
