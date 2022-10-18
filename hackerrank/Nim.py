
# Please implement the game "Nim" and 2 computer players.

# Nim is a two-player game which has a board made up of rows of sticks which looks like this:

# #1: |
# #2: |||
# #3: |||||
# #4: |||||||
# Both players take turns. On each turn, they can remove as many sticks as they would like, as long as they are all on the same row. Whoever removes the last stick from the entire board wins.

# To start, two players will take turns using the same strategy for removing sticks.
# Strategy: Always remove the largest even number (if possible, otherwise just remove 1) of sticks from the first non-empty row.

# After each turn:

# Print the board in a similar format to above
# Print: Player #{n} removed {n} sticks from row {n}
# When a player wins:

# Print: Player #{n} won
# Board can be represented however you wish.

# [execution time limit] 4 seconds (py3)

# =================================================

# Implement a better strategy for player #2:

# * Use brute force to test each possible move to see if it will guarantee a win.
# * We test a possible move by:
#   ** XOR the number of sticks in each row of the resulting board together.
#   ** If the result is equal to 0, then this move will guarantee a win.
# * If there are no moves that guarantee a win, fallback to the previous strategy.

# Example:
# Imagine we had this board after making the move we are testing:
# |
# ||
# ||||
# |||

# If we XOR all the rows together:
# 1 XOR 2 XOR 4 XOR 3

# We get 4, which is not 0, so this is not a winning move.

# XOR is associative and symmetric.

# 0 is the identity for XOR, meaning that 0 XOR anything is itself.

class Nim:
    
    board = []
    current_player = '1'
    sticks_count = 0
    row_num = 0
    move_num = 0
    
    def __init__(self) -> None:
        self.board = []
        # filling board
        for row in range(1, 5):
            self.board.append([1]*(row*2 - 1))
    
    def print_board(self):
        stick_sym = "|"
        for i, row in enumerate(self.board):
            line = "#%s: %s" % ((i+1),  (stick_sym + " ") * len(row))
            print(line)
        
    def print_move_results(self):
        print("Move %s" % self.move_num)
        print("Player #%s removed %s sticks from row %s" % (self.player, self.sticks_count, self.row_num))
        self.print_board()
        print("================================")

           
    def make_turn(self):
        if self.player == '2' and self.bruteforce_better_move():
            pass
        else:
            self.regular_move()

        empty = True
        for row in self.board:
            if len(row) > 0:
                empty = False
                break
        return empty

    def regular_move(self):
        for i, row in enumerate(self.board):
            if len(row) == 0:
                continue
            if len(row) == 1:
                self.board[i] = []
                self.sticks_count = 1
                self.row_num = i + 1
                break
            elif len(row) % 2 == 0:
                self.board[i] = []
                self.sticks_count = len(row)
                self.row_num = i + 1
                break
            else:
                self.board[i] = [1]
                self.sticks_count = len(row) - 1
                self.row_num = i + 1
                break
        self.print_move_results()

    def bruteforce_better_move(self):
        new_board = self.board.copy()
        for r, row in enumerate(self.board):
            self.row_num = r + 1
            new_board[r] = self.board[r].copy()
            for self.sticks_count in range(1, len(row) + 1):
                new_board[r].pop()
                if self.is_win(new_board):
                    self.board = new_board
                    self.print_move_results()
                    return True
            new_board[r] = self.board[r].copy()
        return False
            

    def is_win(self, board):
        res = 0
        for i, row in enumerate(board):
            res ^= len(row)
        if res == 0:
            return True
        return False
    
    def play(self):
        print("Initial board:")    
        self.print_board()

        is_empty = False
        self.player = '1'
        self.move_num = 1
        while not is_empty:
            is_empty = self.make_turn()
            if is_empty:
                print("Player #%s won" % self.player)
            if self.player == '1':
                self.player = '2'
            else:
                self.player = '1'
            self.move_num += 1
        

if __name__ == "__main__":
    nim = Nim()
    nim.play()
        


#1 ^ 3

