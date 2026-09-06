def search(x, seq):
    if not seq:  # Handle empty sequence
        return 0

    for i, value in enumerate(seq):
        if value >= x:
            return i

    return len(seq)