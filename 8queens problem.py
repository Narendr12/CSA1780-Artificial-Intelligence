def solve_n_queens(n):
    def backtrack(row, queens, columns, diagonals1, diagonals2):
        if row == n:
            result.append(queens[:])
            return
        for col in range(n):
            if col in columns or (row - col) in diagonals1 or (row + col) in diagonals2:
                continue
            queens[row] = col
            columns.add(col)
            diagonals1.add(row - col)
            diagonals2.add(row + col)
            backtrack(row + 1, queens, columns, diagonals1, diagonals2)
            columns.remove(col)
            diagonals1.remove(row - col)
            diagonals2.remove(row + col)
    result = []
    queens = [-1] * n
    backtrack(0, queens, set(), set(), set())
    solutions = []
    for sol in result:
        board = []
        for col in sol:
            board.append("." * col + "Q" + "." * (n - col - 1))
        solutions.append(board)
    return solutions
n = 8
solutions = solve_n_queens(n)
print("Number of solutions:", len(solutions))
print("First solution:")
for row in solutions[0]:
    print(row)
