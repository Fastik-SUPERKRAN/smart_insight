"""Solve 3x3 linear equation."""
# TODO a lot of shit :(
import numpy as np


def make_value(matrix: np.ndarray, target_row: int, source_row: int, column: int, target_value: int) -> None:
    """
    Add multiplied source_row to target_row to get value of matrix[target_row][column] to target_value.

    Notes
    -----
    All changes are done inline.
    """
    initial_value = matrix[target_row][column]
    change = target_value - initial_value
    matrix[target_row] = matrix[target_row] + (matrix[source_row] * (change / matrix[source_row][column]))

    # matrix[target_row][column] == value
    # change = target_value - value
    # matrix[target_row][column] = value + (source_value * (change / source_value))
    return


def solve_3_3_equation(A: list[list[float]], B: list[float]) -> np.ndarray:
    """Solve 3x3 linear equation."""
    if not isinstance(A, list) or not isinstance(B, list):
        raise ValueError

    A_np = np.array(A, dtype=float)
    B_np = np.array(B, dtype=float)

    if A_np.shape != (3, 3):
        raise ValueError()
    if B_np.shape == (3,):
        B_np = B_np.reshape(3, 1)
    if B_np.shape != (3, 1):
        raise ValueError()

    matrix = np.concatenate((A_np, B_np), axis=1)

    # search if any row have leading 1
    for row in range(1, len(matrix)):
        if matrix[row][0] == 1:
            matrix[[0, row]] = matrix[[row, 0]]
            break

    # first diagonal 1
    if matrix[0][0] == 0:
        for row in range(1, len(matrix)):
            if matrix[row][0] != 0:
                make_value(matrix, target_row=0, source_row=row, column=0, target_value=1)  # FIXME move to swap
    if matrix[0][0] != 1:
        matrix[0] = matrix[0] * (1 / matrix[0][0])  # FIXME move to mutate_row

    make_value(matrix, target_row=1, source_row=0, column=0, target_value=0)
    make_value(matrix, target_row=2, source_row=0, column=0, target_value=0)

    # second diagonal 1
    if matrix[1][1] == 0:
        for row in range(len(matrix)):
            if matrix[row][1] != 0:
                make_value(matrix, target_row=1, source_row=row, column=1, target_value=1)  # FIXME move to swap
    if matrix[1][1] != 1:
        matrix[1] = matrix[1] * (1 / matrix[1][1])  # FIXME move to mutate_row
    make_value(matrix, target_row=2, source_row=1, column=1, target_value=0)

    # third diagonal 1
    if matrix[2][2] == 0:
        for row in range(len(matrix)):
            if matrix[row][2] != 0:
                make_value(matrix, target_row=2, source_row=row, column=2, target_value=1)  # FIXME move to swap
    if matrix[2][2] != 1:
        matrix[2] = matrix[2] * (1 / matrix[2][2])  # FIXME move to mutate_row

    # Echelon form is done ╰(*°▽°*)╯

    make_value(matrix, target_row=1, source_row=2, column=2, target_value=0)
    make_value(matrix, target_row=0, source_row=2, column=2, target_value=0)
    make_value(matrix, target_row=0, source_row=1, column=1, target_value=0)

    return matrix[::, 3]


if __name__ == '__main__':
    A = [[1, 2, 3], [0, 1, 2], [2, 0, 0]]
    B = [1, 1, 0]
    print(solve_3_3_equation(A, B))
