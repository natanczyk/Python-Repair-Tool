def next_permutation(perm):
    # Find the largest index i such that perm[i] < perm[i + 1]
    for i in range(len(perm) - 2, -1, -1):
        if perm[i] < perm[i + 1]:
            # Find the largest index j > i such that perm[i] < perm[j]
            for j in range(len(perm) - 1, i, -1):
                if perm[j] > perm[i]:
                    # Create a mutable copy of the permutation
                    next_perm = list(perm)
                    # Swap the value at index i with that at j
                    next_perm[i], next_perm[j] = next_perm[j], next_perm[i]
                    # Reverse the suffix starting at i + 1
                    next_perm[i + 1:] = reversed(next_perm[i + 1:])
                    return next_perm