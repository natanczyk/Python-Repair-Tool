def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original
    remaining = lst[:]
    op = []
    count = 0
    while count < k:
        if not remaining:
            break
        big = max(remaining)
        op.append(big)
        # Remove one occurrence of the maximum value
        remaining.remove(big)
        count += 1
    return op