def search(x, seq):
    """
    Sequential search to find the index where x should be inserted in seq.
    Returns the index of the first element >= x, or len(seq) if x is greater than all elements.
    """
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
    return len(seq)