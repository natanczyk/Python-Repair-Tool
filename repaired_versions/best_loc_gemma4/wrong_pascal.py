def pascal(n):
    rows = [[1]]
    for r in range(1, n):
        row = []
        # The r-th row (0-indexed) has r + 1 elements
        for c in range(0, r + 1):
            # Value is the sum of the two values above it in the previous row
            upleft = rows[r - 1][c - 1] if c > 0 else 0
            upright = rows[r - 1][c] if c < len(rows[r - 1]) else 0
            row.append(upleft + upright)
        rows.append(row)

    return rows