def next_permutation(perm):
    # Find the longest non-increasing suffix and find the pivot
    pivot = -1
    for i in range(len(perm) - 1, 0, -1):
        if perm[i - 1] < perm[i]:
            pivot = i
            break
    
    if pivot == -1:
        return perm[::-1]  # The entire array is non-increasing
    
    # Find the rightmost successor to the pivot
    for i in range(len(perm) - 1, pivot - 1, -1):
        if perm[i] > perm[pivot - 1]:
            perm[pivot - 1], perm[i] = perm[i], perm[pivot - 1]
            break
    
    # Reverse the suffix
    perm[pivot:] = reversed(perm[pivot:])
    
    return perm