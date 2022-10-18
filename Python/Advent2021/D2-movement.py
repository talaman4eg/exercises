#!/usr/bin/python3
def movement1(data):
    pos = [0, 0]
    for line in data:
        (k, v) = line.strip().split()
        v = int(v)
        if k == 'forward':
            pos[0] += v
        elif k =='up':
            pos[1] -= v
        elif k == 'down':
            pos[1] += v

    return pos[0]*pos[1]

def movement2(data):
    pos = [0, 0]
    aim = 0
    for line in data:
        (k, v) = line.strip().split()
        v = int(v)
        if k == 'forward':
            pos[0] += v
            pos[1] += aim * v
        elif k =='up':
            aim -= v
        elif k == 'down':
            aim += v

    return pos[0]*pos[1]


filename = 'D2-data.txt'
f = open(filename)
try:
    data = f.readlines()
    print(movement2(data))
finally:
    f.close()


