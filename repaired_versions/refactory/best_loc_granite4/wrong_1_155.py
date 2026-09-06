def search(x, seq):
    if not seq:  # Check for any empty sequence type
        return 0
    for index, value in enumerate(seq):
        if x <= value:
            return index
    return len(seq)