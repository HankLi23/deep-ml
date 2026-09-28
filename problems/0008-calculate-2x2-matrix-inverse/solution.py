def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    a = matrix[0][0]
    b = matrix[0][1]
    c = matrix[1][0]
    d = matrix[1][1]
    
    det = a * d - b * c
    if det == 0:
        return None
    
    inv_det = 1 / det
    inv_matrix = [
        [d * inv_det, -b * inv_det],
        [-c * inv_det, a * inv_det]
    ]
    return inv_matrix