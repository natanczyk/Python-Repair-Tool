def pascal(n):
    rows = [[1]]
    for r in range(1, n):
        row = [1]
        for c in range(1, r):
            row.append(rows[r - 1][c - 1] + rows[r - 1][c])
        row.append(1)
        rows.append(row)

    return rows