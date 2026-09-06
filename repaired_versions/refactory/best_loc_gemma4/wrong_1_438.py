def search(x, seq):
    """
    Returns the index of the first element in seq that is not less than x.
    If all elements are less than x, returns the length of the sequence.
    """
    for i in range(len(seq)):
        if seq[i] >= x:
            return i
    return len(seq)