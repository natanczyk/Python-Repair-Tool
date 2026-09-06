def search(x, seq):
    if not seq:  # Check for empty sequence
        return 0
    for i, val in enumerate(seq):
        if val >= x:
            return i
    return len(seq)