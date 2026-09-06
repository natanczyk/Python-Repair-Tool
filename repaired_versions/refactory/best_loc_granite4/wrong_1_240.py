def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    n = len(seq)
    for i in range(n):
        if x <= seq[i]:
            return i
    return n  # Return n if x is greater than all elements