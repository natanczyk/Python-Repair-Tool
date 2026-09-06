def search(x, seq):
    n = len(seq)
    result = n  # Initialize result to the length of the sequence
    for counter in range(n):
        if seq[counter] >= x:
            result = counter
            break
    return result