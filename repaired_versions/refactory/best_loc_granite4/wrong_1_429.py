def search(x, seq):
    if not seq:  # Handle empty sequence
        return 0
    for i, elem in enumerate(seq):
        if elem >= x:
            return i
    return len(seq)