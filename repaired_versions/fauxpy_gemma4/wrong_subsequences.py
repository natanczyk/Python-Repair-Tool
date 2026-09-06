def subsequences(a, b, k):
    if k == 0:
        return [[]]

    ret = []
    # The range of integers is range(a, b), so the maximum value is b-1.
    # To have k elements starting from i, i must be at most (b-1) - (k-1) = b - k.
    for i in range(a, b - k + 1):
        for rest in subsequences(i + 1, b, k - 1):
            ret.append([i] + rest)

    return ret