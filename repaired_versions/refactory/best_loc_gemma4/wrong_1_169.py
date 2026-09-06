def search(x, seq):
    """
    Returns the index of the first element in seq that is greater than or equal to x.
    If no such element exists, returns the length of the sequence.
    """
    for i, element in enumerate(seq):
        if x <= element:
            return i
    return len(seq)