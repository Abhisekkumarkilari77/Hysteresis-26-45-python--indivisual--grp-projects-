# 35. Sudoku Solver

def solve(board):
    empty = find_empty(board)
    if not empty: return True
    r, c = empty
    for num in map(str, range(1,10)):
        if valid(board, r, c, num):
            board[r][c] = num
            if solve(board): return True
            board[r][c] = "."
    return False

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".": return (i,j)
    return None

def valid(board, r, c, num):
    row = num not in board[r]
    col = num not in [board[i][c] for i in range(9)]
    box = num not in [board[i][j] for i in range(r//3*3, r//3*3+3) for j in range(c//3*3, c//3*3+3)]
    return row and col and box

if __name__ == "__main__":
    puzzle = [list("53..7...."), list("6..195..."), list(".98....6."), list("8...6...3"),
              list("4..8.3..1"), list("7...2...6"), list(".6....28."), list("...419..5"), list("....8..79")]
    solve(puzzle)
    for row in puzzle: print("".join(row))
