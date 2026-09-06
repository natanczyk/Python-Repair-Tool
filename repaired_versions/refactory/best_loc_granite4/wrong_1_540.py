def search(x, seq):
    if not seq:  # Check for any empty sequence
        return 0
    for i in range(len(seq)):
        if seq[i] >= x:
            return i
    return len(seq)