def search(x, seq):
    if not seq:
        return 0
    left, right = 0, len(seq)
    while left < right:
        mid = (left + right) // 2
        if seq[mid] < x:
            left = mid + 1
        else:
            right = mid
    return left