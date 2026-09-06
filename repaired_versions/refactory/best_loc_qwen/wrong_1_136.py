def search(x, seq):
    left, right = 0, len(seq)
    
    while left < right:
        mid = (left + right) // 2
        if seq[mid] < x:
            left = mid + 1
        else:
            right = mid
    
    return left