def next_permutation(perm):
    # Find the largest index i such that perm[i] < perm[i + 1]
    for i in range(len(perm) - 2, -1, -1):
        if perm[i] < perm[i + 1]:
            # Find the largest index j greater than i such that perm[i] < perm[j]
            for j in range(len(perm) - 1, i, -1):
                if perm[j] > perm[i]:
                    # Swap perm[i] and perm[j]
                    next_perm = list(perm)
                    next_perm[i], next_perm[j] = next_perm[j], next_perm[i]
                    # Reverse the sequence from perm[i + 1] to the end
                    next_perm[i + 1:] = reversed(next_perm[i + 1:])
                    return next_perm