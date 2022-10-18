if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    res = []
    
    [[[res.append([i, j, k]) if i + j + k != n else 0 for i in range(0, x+1)] for j in range(0, y+1)] for k in range(0, z+1)]
    
    print(res)
    