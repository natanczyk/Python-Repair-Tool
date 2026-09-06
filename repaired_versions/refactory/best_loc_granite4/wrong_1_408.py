def search(x, seq):
    if not seq:  # Check for empty sequence first
        return 0
    for i, value in enumerate(seq):
        if x <= value:
            return i
    return len(seq)  # x is greater than all elements