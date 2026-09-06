def next_permutation(perm):
    # Find the longest non-increasing suffix and find the pivot
    pivot = -1
    for i in range(len(perm) - 2, -1, -1):
        if perm[i] < perm[i + 1]:
            pivot = i
            break
    
    if pivot == -1:
        return perm[::-1]  # The entire array is non-increasing
    
    # Find the rightmost successor to the pivot
    for j in range(len(perm) - 1, pivot, -1):
        if perm[j] > perm[pivot]:
            perm[pivot], perm[j] = perm[j], perm[pivot]
            break
    
    # Reverse the suffix
    perm[pivot + 1:] = reversed(perm[pivot + 1:])
    
    return perm