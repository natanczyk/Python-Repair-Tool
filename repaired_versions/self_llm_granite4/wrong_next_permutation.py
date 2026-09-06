def next_permutation(perm):
    for i in range(len(perm) - 2, -1, -1):
        if perm[i] < perm[i + 1]:
            for j in range(len(perm) - 1, i, -1):
                if perm[j] > perm[i]:  # use > to find the smallest larger element
                    next_perm = list(perm)
                    next_perm[i], next_perm[j] = next_perm[j], next_perm[i]
                    next_perm[i + 1:] = reversed(next_perm[i + 1:])  # reversed returns an iterator, which can be assigned to a slice
                    return next_perm
    # If no next permutation (should not happen due to precondition), return the sorted (ascending) permutation
    return sorted(perm)