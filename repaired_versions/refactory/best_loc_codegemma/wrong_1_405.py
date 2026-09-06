def search(x, seq):
    for i in range(len(seq)):
        if seq[i] >= x:
            return i
    if not seq:  # Check if the sequence is empty
        return 0  # Return 0 for empty sequences
    return len(seq)