#!/usr/bin/python

def debug(*argv):
    print(argv)
    pass

def do_steps(src):
    moves = [
        10, 17,
        15, 6,
        -10, -17,
        -6, -15]

    if src % 8 < 2:
        if -10 in moves: moves.remove(-10)
        if 6 in moves: moves.remove(6)
    if src % 8 < 1:
        if -17 in moves: moves.remove(-17)
        if 15 in moves: moves.remove(15)
    if src % 8 > 6:
        if -15 in moves: moves.remove(-15)
        if 17 in moves: moves.remove(17)
    if src % 8 > 5:
        if -6 in moves: moves.remove(-6)
        if 10 in moves: moves.remove(10)
    if src < 8:
        if -10 in moves: moves.remove(-10)
        if -6 in moves: moves.remove(-6)
    if src < 16:
        if -17 in moves: moves.remove(-17)
        if -15 in moves: moves.remove(-15)
    if src > 55:
        if 10 in moves: moves.remove(10)
        if 6 in moves: moves.remove(6)
    if src > 47:
        if 15 in moves: moves.remove(15)
        if 17 in moves: moves.remove(17)

    points = []

    for m in moves:
        points.append(src + m)

    return points



def solution(src, dest):

    if src == dest:
        return 0
    max_steps = 1000

    step = 0
    new_points = [src]

    while step < max_steps:
        step += 1
        current_points = new_points
        debug(current_points)
        new_points = []
        for cur_point in current_points:
            moves = do_steps(cur_point)
            for point in moves:
                if point == dest:
                    return step
                if point not in new_points:
                    new_points.append(point)




    raise Exception("Max steps %s exceeded" % max_steps)



if __name__ == '__main__':

    print(solution(7, 7))
    print('\n')
