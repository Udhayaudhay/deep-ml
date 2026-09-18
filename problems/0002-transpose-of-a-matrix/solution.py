def transpose_matrix(a: list[list[int | float]]) -> list[list[int | float]]:
    rows = len(a)
    cols = len(a[0])
    result = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(a[i][j])
        result.append(row)
    return result