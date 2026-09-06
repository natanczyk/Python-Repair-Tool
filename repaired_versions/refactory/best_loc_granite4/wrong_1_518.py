def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    for c, value in enumerate(seq):
        if value >= x:
            return c
    else:
        return len(seq)