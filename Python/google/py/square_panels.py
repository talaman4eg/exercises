#!/usr/bin/python
def solution(area):
    squares = []
    res = []
    i = 1
    sq = 1
    while sq <= area and i <= 1001:
        squares.append(sq)
        sq = i*i
        i += 1
    print squares
    while area > 0:
        while squares[len(squares) - 1] > area:
            squares.pop()
            #print squares
        res.append(squares[len(squares) - 1])
        area -= squares[len(squares) - 1]

    return res


if __name__ == '__main__':

    print(solution(1000000))
    print('\n')
