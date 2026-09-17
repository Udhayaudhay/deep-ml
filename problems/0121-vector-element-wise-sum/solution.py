def vector_sum(a, b):
    if len(a) != len(b):
        return -1

    result = []

    for i in range(len(a)):
        result.append(a[i] + b[i])

    return result