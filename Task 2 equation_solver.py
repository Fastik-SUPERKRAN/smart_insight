"""Solve linear equations using Gaussian elimination."""
# Standart library imports
import pprint
from copy import deepcopy

import numpy as np


def make_value(matrix: np.ndarray, target_row: int, source_row: int, column: int, target_value: float) -> np.ndarray:
    """Add multiplied source_row to target_row to get value of matrix[target_row][column] to target_value.

    Parameters
    ----------
    matrix : np.ndarray
        Source matrix.
    target_row : int
        Number of target row.
    source_row : int
        Number of source row.
    column : int
        Column of target value.
    target_value : float
        Target value.

    Returns
    -------
    np.ndarray
        Changed matrix.
    """
    changed_matrix = deepcopy(matrix)

    initial_value = changed_matrix[target_row][column]
    change = target_value - initial_value

    changed_matrix[target_row] = changed_matrix[target_row] + (
        changed_matrix[source_row] * (change / changed_matrix[source_row][column])
    )

    return changed_matrix


def swap_rows(matrix: np.ndarray, source_row: int, target_row: int) -> np.ndarray:
    """Swap the positions of two rows.

    Parameters
    ----------
    matrix : np.ndarray
        Source matrix.
    source_row : int
        Number of source row.
    target_row : int
        Number of target row.

    Returns
    -------
    np.ndarray
        Matrix with rows swapped.
    """
    changed_matrix = deepcopy(matrix)

    changed_matrix[[source_row, target_row]] = changed_matrix[[target_row, source_row]]

    return changed_matrix


def mutate_row(matrix: np.ndarray, row: int, column: int, target_value: float) -> np.ndarray:
    """Multiply a row by a non-zero scalar to get target value at matrix[row][column].

    Parameters
    ----------
    matrix : np.ndarray
        Source matrix.
    row : int
        Row of target.
    column : int
        Column of target.
    target_value : float
        Value we need at matrix[row][column].

    Returns
    -------
    np.ndarray
        Mutated matrix.
    """
    changed_matrix = deepcopy(matrix)

    changed_matrix[row] = changed_matrix[row] * (target_value / changed_matrix[row][column])

    return changed_matrix


def solve_linear_equation(A: list[list[float]], B: list[float]) -> np.ndarray:
    """Solve linear equation using Gaussian elimination.

    Parameters
    ----------
    A : list of list
        Input equations.
    B : list of float
        Input equation results.

    Returns
    -------
    np.ndarray
        Array of equation result.

    Raises
    ------
    ValueError
        If input values are not list.
    ValueError
        if "A" matrix is not square.
    ValueError
        If "B" matrix does not have same number of rows.
    ValueError
        If "A" matrix have zero rows or columns.
    """
    if not isinstance(A, list) or not isinstance(B, list):
        raise ValueError('Inputs must be lists')

    A_np = np.array(A, dtype=float)
    B_np = np.array(B, dtype=float)

    if A_np.shape[0] != A_np.shape[1]:
        raise ValueError(f'"A" matrix should be square: ({A_np.shape[0]}, {A_np.shape[1]})')
    if B_np.shape == (A_np.shape[0],):
        B_np = B_np.reshape(A_np.shape[0], 1)
    if B_np.shape != (A_np.shape[0], 1):
        raise ValueError(f'"B" matrix should have same number of rows: {B_np.shape[0]} != {A_np.shape[0]}')
    if not all(any(row) for row in A_np) or not all(any(column) for column in A_np.T):
        raise ValueError('Matrix have zero row or column.')

    # create augmented matrix
    matrix = np.concatenate((A_np, B_np), axis=1)

    # forward elimination
    for row, column in zip(range(matrix.shape[1] - 1), range(matrix.shape[0])):

        # check if diagonal value is 0, and swap it with row that has nonzero value at the same column
        if matrix[row][column] == 0:
            for tmp_row in range(row + 1, matrix.shape[0]):
                if matrix[tmp_row][0] != 0:
                    matrix = swap_rows(matrix, source_row=tmp_row, target_row=row)

        # make diagonal value equal to 1
        if matrix[row][column] != 1:
            matrix = mutate_row(matrix, row=row, column=column, target_value=1)

        # make other entries in column lower than diagonal value zeros
        for tmp_row in range(row + 1, matrix.shape[0]):
            matrix = make_value(matrix, target_row=tmp_row, source_row=row, column=column, target_value=0)

    # Echelon form is done ╰(*°▽°*)╯

    # back substitution
    for row_number in range(matrix.shape[0] - 2, 0 - 1, -1):
        for next_row_number in range(row_number + 1, matrix.shape[0]):
            matrix = make_value(
                matrix, target_row=row_number, source_row=next_row_number, column=next_row_number, target_value=0
            )

    return matrix[..., -1]


if __name__ == '__main__':
    pp = pprint.PrettyPrinter()
    # reduce number of symbols after dot when printing numpy array
    np.set_printoptions(precision=3)

    A = [[1, 2, 3], [0, 1, 2], [2, 0, 0]]
    B = [1, 1, 0]

    print('Input matrixes')
    pp.pprint(A)
    pp.pprint(B)
    print('Result')
    pp.pprint(solve_linear_equation(A, B))

    # some additional test equation
    print('Some additional test equation')
    A = [[1, 2, 3, 1, 3], [0, 1, 2, 1, 2], [2, 0, 0, 0, 1], [0, 4, 2, 2, 3], [5, 6, 7, 2, 5]]
    B = [3, 5, 4, 6, 7]

    print('Input matrixes')
    pp.pprint(A)
    pp.pprint(B)
    print('Result')
    pp.pprint([round(i, 3) for i in solve_linear_equation(A, B)])
    print('Correct solution')
    pp.pprint([round(i, 3) for i in [7 / 3, -3.0, -2 / 3, 32 / 3, -2 / 3]])
