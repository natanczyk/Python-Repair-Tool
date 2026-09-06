def search(x, seq):
    if not seq:  # Handle empty sequence
        return 0
    for i, value in enumerate(seq):
        if x < value:
            return i
        elif x == value:
            return i
    return len(seq)  # x is greater than all elements