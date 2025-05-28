def print_solution(board, n):
    for i in range(n):
        for j in range(n):
            print("Q" if board[i][j] else ".", end=" ")
        print()
    print()


def is_safe(board, row, col, n):
    # Check this row on the left
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on the left
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on the left
    i, j = row, col
    while i < n and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1

    return True


def solve_n_queens_util(board, col, n):
    if col >= n:
        print_solution(board, n)
        return True

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = True
            res = solve_n_queens_util(board, col + 1, n) or res
            board[i][col] = False  # Backtrack

    return res


def solve_n_queens(n):
    board = [[False for _ in range(n)] for _ in range(n)]
    if not solve_n_queens_util(board, 0, n):
        print("No solution exists for", n, "Queens")


# You can test with any number of queens:
n = 4
solve_n_queens(n)