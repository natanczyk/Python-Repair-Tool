def search(x, seq):
    low = 0
    high = len(seq)
    while low < high:
        mid = (low + high) // 2
        if seq[mid] < x:
            low = mid + 1
        else:
            high = mid
    return low