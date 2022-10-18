#!/usr/bin/python3
def power1(data):
    num_len = len(data[0].strip())
    data_len = len(data)
    stat = [0]*num_len
    for line in data:
        for i in range(num_len):
            if line[i] == '1':
                stat[i] += 1


    gamma = ['0']*num_len
    eps = ['1']*num_len

    for i in range(num_len):
        if(stat[i] > data_len/2):
            gamma[i] = '1'
            eps[i] = '0'



    return int(''.join(gamma), 2) * int(''.join(eps), 2)


def count_bits(data, position):
    ones = 0
    zeros = 0
    for num in data:
        if num[position] == '1':
            ones += 1
        else:
            zeros += 1
    return (zeros, ones)


def oxy(data):
    ogr = []
    csr = []

    num_len = len(data[0])


    ogr = data[:]
    for i in range(num_len):
        (zeros, ones) = count_bits(ogr, i)

        if zeros > ones:
            keep = '0'
        else:
            keep = '1'
        ogr = list([x for x in ogr if x[i] == keep])
        if len(ogr) == 1:
            break;

    csr = data[:]
    for i in range(num_len):
        (zeros, ones) = count_bits(csr, i)
        print(zeros, ones)

        if zeros <= ones:
            keep = '0'
        else:
            keep = '1'
        csr = list([x for x in csr if x[i] == keep])
        if len(csr) == 1:
            break;


    return int(''.join(ogr[0]), 2) * int(''.join(csr[0]), 2)


filename = 'D3-data.txt'
f = open(filename)
try:
    data = f.readlines()
    
    print(oxy([x.strip() for x in data]))
finally:
    f.close()


