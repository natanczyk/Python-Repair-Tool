def pascal(n):
    rows = [[1]]
    for r in range(1, n):
        row = [1]  # First element is always 1
        for c in range(1, r):
            upleft = rows[r - 1][c - 1] if c > 0 else 0
            upright = rows[r - 1][c] if c < r else 0
            row.append(upleft + upright)
        row.append(1)  # Last element is always 1
        rows.append(row)

    return rows