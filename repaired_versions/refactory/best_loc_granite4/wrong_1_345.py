def search(x, seq):
    if not seq:  # Check for any empty sequence (list or tuple)
        return 0
    for i, value in enumerate(seq):
        if x == value:
            return i
        elif x < value:
            return i
    return len(seq)