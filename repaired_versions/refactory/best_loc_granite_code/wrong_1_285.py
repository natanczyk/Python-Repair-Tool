def search(x, seq):
    if len(seq) == 0:
        return 0
    left = 0
    right = len(seq) - 1
    while left <= right:
        mid = (left + right) // 2
        if seq[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return left