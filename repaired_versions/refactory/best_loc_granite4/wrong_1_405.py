def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    for i in range(len(seq)):
        if seq[i] >= x:
            return i
    return len(seq)