def search(x, seq):
    if not seq:  # Handle empty sequence
        return 0
    for i in range(len(seq)):
        if seq[i] >= x:
            return i
    return len(seq)