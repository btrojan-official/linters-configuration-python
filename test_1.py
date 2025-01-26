import numpy as np
from main import calculate_inverse

# Test the function with assert statements
def test_calculate_inverse():
    # Test 1: Identity matrix
    identity = np.eye(3)
    assert np.allclose(calculate_inverse(identity), identity), "Test 1 Failed"

    # Test 2: Simple 2x2 matrix
    matrix_2x2 = np.array([[4, 7], [2, 6]])
    inverse_2x2 = np.array([[0.6, -0.7], [-0.2, 0.4]])
    assert np.allclose(calculate_inverse(matrix_2x2), inverse_2x2), "Test 2 Failed"

    # Test 3: Random 3x3 matrix
    matrix_3x3 = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
    inverse_3x3 = np.array([[-24, 18, 5], [20, -15, -4], [-5, 4, 1]]) / 1.0
    assert np.allclose(calculate_inverse(matrix_3x3), inverse_3x3), "Test 3 Failed"

    # Test 4: Verify inverse property (A * A^-1 = I)
    matrix_4x4 = np.random.rand(4, 4)
    inverse_4x4 = calculate_inverse(matrix_4x4)
    identity_4x4 = np.dot(matrix_4x4, inverse_4x4)
    assert np.allclose(identity_4x4, np.eye(4)), "Test 4 Failed"