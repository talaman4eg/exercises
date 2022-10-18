#!/usr/bin/python3

class Advent:

    filename = "D4.txt"
    def solve(data):
        return Advent.d4_2(data)


    def d4_calc_score(board, num):
        res = 0
        for row in board:
            for val in row:
                if val[1] == 0:
                    res += val[0]
        return res * num

    def d4_read_boards(data):
        numbers = [int(x) for x in data[0].strip().split(',')]
        boards = []
        board = []

        for i in range(2, len(data)):
            line = data[i].strip()
            if line == '':
                boards.append(board)
                board = []
            else:
                board.append(list([[int(x), 0] for x in line.split()]))
        if len(board) > 0:
            boards.append(board)
        return (numbers, boards)

    def d4_1(data):
        (numbers, boards) = Advent.d4_read_boards(data)
        for num in numbers:
            for board in boards:
                for row in range(0, len(board)):
                    for col in range(0, len(board[row])):
                        if board[row][col][0] == num:
                            board[row][col][1] = 1
                            winner = True
                            for r in range(0, len(board)):
                                if board[r][col][1] == 0:
                                    winner = False
                                    break
                            if winner:
                                return Advent.d4_calc_score(board, num)
                            for c in range(0, len(board[row])):
                                if board[row][c][1] == 0:
                                    winner = False
                                    break
                            if winner:
                                return Advent.d4_calc_score(board, num)
        return ''

    def d4_2(data):
        (numbers, boards) = Advent.d4_read_boards(data)
        loosers = list(range(0, len(boards)))
        for num in numbers:
            for b in range(0, len(boards)):
                board = boards[b]
                for row in range(0, len(board)):
                    for col in range(0, len(board[row])):
                        if board[row][col][0] == num:
                            board[row][col][1] = 1
                            winner = True
                            for r in range(0, len(board)):
                                if board[r][col][1] == 0:
                                    winner = False
                                    break
                            if winner:
                                if len(loosers) > 1:
                                    if b in loosers:
                                        loosers.remove(b)
                                else:
                                    return Advent.d4_calc_score(board, num)
                            for c in range(0, len(board[row])):
                                if board[row][c][1] == 0:
                                    winner = False
                                    break
                            if winner:
                                if len(loosers) > 1:
                                    if b in loosers:
                                        loosers.remove(b)
                                else:
                                    return Advent.d4_calc_score(board, num)
        return ''






if __name__ == "__main__":
    f = open(Advent.filename)
    try:
        data = f.readlines()
        print(Advent.solve(data))
    finally:
        f.close()



