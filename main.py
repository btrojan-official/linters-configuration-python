import numpy as np

def calculate_inverse(matrix):
    """
    Calculates the inverse of a given square matrix.

    Parameters:
    matrix (numpy.ndarray): A square matrix to invert.

    Returns:
    numpy.ndarray: The inverse of the matrix.
    """
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square.")
    return np.linalg.inv(matrix)