def search(x, seq):
    if not seq:  # Handle empty sequence
        return 0
    for index, value in enumerate(seq):
        if x <= value:
            return index
    return len(seq)