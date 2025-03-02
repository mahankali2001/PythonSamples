class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = len(board)    
        cols = len(board[0])
        # print(rows, cols)
        # sudokovals = {}
        for i, slist in enumerate(board):
            seen = set()
            for j, val in enumerate(slist):
                print("row - {}, column - {}, value - {}".format(i, j,val))
                if val == ".":
                    continue
                if val in seen:
                    print(seen)
                    print("found repetition in the row - {}, column - {}".format(i,j))
                    return False
                seen.add(val)
                # sudokovals[(i,j)] = val
        
        for c in range(cols):
            seen = set()
            for r in range(rows):
                print("column - {}, row - {}, value - {}".format(c, r, board[r][c]))
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    print(seen)
                    print("found repetition in the column - {}, row - {}".format(c, r))
                    return False
                seen.add(board[r][c])
                # sudokovals[(i,j)] = val
        
        for square in range(rows):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    print("square - {}, row - {}, column - {}, value - {}".format(square, row, col, board[row][col]))
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        print(seen)
                        print("found repetition in the square - {}: row - {}, column - {}, value - {}".format(square, row, col,  board[row][col]))
                        return False
                    seen.add(board[row][col])
                    # sudokovals[(i,j)] = val
        
        return True

        print(sudokovals)

if __name__ == "__main__":
    s = Solution()
#     print(s.isValidSudoku([
#  ["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]))
    
#     print(s.isValidSudoku([
#  ["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","1",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]))
        

    print(s.isValidSudoku(
    [[".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".","9",".",".",".",".",".",".","1"],
    ["8",".",".",".",".",".",".",".","."],
    [".","9","9","3","5","7",".",".","."],
    [".",".",".",".",".",".",".","4","."],
    [".",".",".","8",".",".",".",".","."],
    [".","1",".",".",".",".","4",".","9"],
    [".",".",".","5",".","4",".",".","."]]))