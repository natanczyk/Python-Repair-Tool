def search(x, seq):
    if not seq:  # Check for empty sequence
        return 0
    if x <= seq[0]:
        return 0
    for i in range(1, len(seq)):
        if x <= seq[i] and x > seq[i-1]:
            return i
    return len(seq)  # Return length if x is greater than or equal to the last element