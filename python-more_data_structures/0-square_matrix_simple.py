def square_matrix_simple(matrix=[]):
    """Return a new matrix with each value squared (does not modify input)."""
    return [[value * value for value in row] for row in matrix]