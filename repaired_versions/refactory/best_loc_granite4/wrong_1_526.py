def search(x, seq):
    if not seq:  # Check for empty sequence
        return 0
    for i, elem in enumerate(seq):
        if x <= elem:
            return i
    return len(seq)