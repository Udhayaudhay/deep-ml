import numpy as np

def reshape_matrix(a, new_shape):
    rows, cols = new_shape

    # Flatten the matrix
    flat = []
    for row in a:
        for value in row:
            flat.append(value)

    # Cannot reshape if element counts don't match
    if len(flat) != rows * cols:
        return []

    # Create new matrix
    result = []

    for i in range(0, len(flat), cols):
        result.append(flat[i:i + cols])

    return result