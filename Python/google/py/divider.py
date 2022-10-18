#!/usr/bin/python
import sys
show_debug = 0
def dbg(*args):
    if show_debug == 1:
        print(args)



def str_inc(num):
    """ Increments integer number represented as list of digits as strings by 1

    >>> str_inc(['2', '3', '4'])
    ['2', '3', '5']

    >>> str_inc(['2', '9', '9'])
    ['3', '0', '0']

    >>> str_inc(['9', '9', '9'])
    ['1', '0', '0', '0']

    """
    val = num[:]
    i = len(val) - 1
    while val[i] == '9':
        val[i] = '0'
        if i == 0:
            val.insert(0, '0')
            break
        i -= 1

    val[i] = str(int(val[i]) + 1)

    return val

def str_dec(num):
    """ Decrements integer number represented as list of digits as strings by 1

    >>> str_dec(['2', '3', '4'])
    ['2', '3', '3']

    >>> str_dec(['2', '0', '0'])
    ['1', '9', '9']

    >>> str_dec(['1', '0', '0'])
    ['9', '9']

    >>> str_dec(['0'])
    Traceback (most recent call last):
        ...
    ValueError: Negative numbers not supported

    >>> str_dec(['0', '0'])
    Traceback (most recent call last):
        ...
    ValueError: Negative numbers not supported

    """
    val = num[:]
    i = len(val) - 1
    while val[i] == '0':
        val[i] = '9'
        if i == 0:
            raise ValueError("Negative numbers not supported")
            break
        i -= 1

    val[i] = str(int(val[i]) - 1)
    if val[0] == '0':
        val.pop(0)

    return val

def str_divide(num):
    """ Divide integer number represented as list of digits as strings by 2

    >>> str_divide(['2', '2', '4'])
    ['1', '1', '2']

    >>> str_divide(['2', '0', '0'])
    ['1', '0', '0']

    >>> str_divide(['3', '0', '0'])
    ['1', '5', '0']

    >>> str_divide(['2', '3', '4'])
    ['1', '1', '7']

    >>> str_divide(['1', '0', '0'])
    ['5', '0']

    >>> str_divide(['2', '3', '5'])
    Traceback (most recent call last):
        ...
    ValueError: Odd numbers not supported

    """
    i = len(num) - 1
    if int(num[i]) % 2 == 1:
        raise ValueError("Odd numbers not supported")

    while i >= 0:
        if int(num[i]) % 2 == 0:
            num[i] = str(int(num[i]) / 2)
        else:
            num[i] = str(int(num[i]) / 2)
            num[i+1] = str(int(num[i+1]) + 5)
        i -= 1

    while num[0] == '0':
        num.pop(0)

    return num


def divider(num):
    """ Divide by 2 until even

    >>> divider(['4'])
    2

    >>> divider(['3'])
    0

    """
    step = 0
    while int(num[len(num) - 1]) % 2 == 0:
        num = str_divide(num)
        step += 1
    return step

def process_recursive(num, step):
    dbg(num, step)
    div_step = divider(num)
    step += div_step

    if num == ['1']:
        return step
    plus = str_inc(num)
    dbg(plus)
    steps_plus = process_recursive(plus, step+1)
    dbg(steps_plus)
    minus = str_dec(num)
    dbg(minus)
    steps_minus = process_recursive(minus, step+1)
    if steps_plus > steps_minus:
        return steps_minus
    else:
        return steps_plus


def process_loop(num):
    step = 0
    cur_step = 0
    while num != ['1']:
        cur_step = divider(num)
        dbg(cur_step, num)
        step += cur_step
        if cur_step == 0:
            plus = str_inc(num)
            steps_plus = divider(plus)
            dbg('plus', plus)
            minus = str_dec(num)
            steps_minus = divider(minus)

            step += 1

            if plus == ['1'] and minus != ['1']:
                return step + steps_plus
            if minus == ['1'] and plus != ['1']:
                return step + steps_minus
            if minus == ['1'] and plus == ['1']:
                if steps_plus < steps_minus:
                    return step + steps_plus
                else:
                    return step + steps_minus

            if steps_plus < steps_minus:
                step += steps_minus
                num = minus
            else:
                step += steps_plus
                num = plus

    return step


def solution(n):
    #return process_recursive(list(n), 0)
    return process_loop(list(n))
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    show_debug = 1
    print(solution(sys.argv[1]))
