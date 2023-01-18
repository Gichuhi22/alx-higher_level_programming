import sys
""" a nqueens algorithm module
"""


def nqueens(n):
    """a function that solves the nqueens puzzle
        arguments:n number of arguments passed
    """
    def solve(row, diagonals1, diagonals2, result, solutions):
        if row == n:
            solutions.append(result)
            return
        for col in range(n):
            d1, d2 = row - col, row + col
            if col not in result and d1 not in diagonals1
            and d2 not in diagonals2:
                solve(row + 1, diagonals1 |
                      {d1}, diagonals2 | {d2}, result + [col], solutions)

    solutions = []
    solve(0, set(), set(), [], solutions)
    for i, solution in enumerate(solutions):
        print("Solution {}:".format(i + 1))
        for r in range(n):
            print(" ".join(".Q" [c == solution[r]] for c in range(n)))
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(n)
