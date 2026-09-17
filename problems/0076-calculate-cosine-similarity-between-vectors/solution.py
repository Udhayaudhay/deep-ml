import numpy as np

def cosine_similarity(v1, v2):
    """
    Return the cosine similarity of two vectors.
    """

    if v1.shape != v2.shape:
        raise ValueError("Vectors must have same shape")

    if v1.size == 0 or v2.size == 0:
        raise ValueError("Vectors cannot be empty")

    if np.linalg.norm(v1) == 0 or np.linalg.norm(v2) == 0:
        raise ValueError("Vectors cannot have zero magnitude")

    return float(
        np.dot(v1, v2) /
        (np.linalg.norm(v1) * np.linalg.norm(v2))
    )