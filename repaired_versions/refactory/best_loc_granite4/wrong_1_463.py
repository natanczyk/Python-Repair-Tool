def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    for i, value in enumerate(seq):
        if x <= value:
            return i
    return len(seq)