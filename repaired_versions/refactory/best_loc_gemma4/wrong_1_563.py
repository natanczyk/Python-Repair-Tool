def search(x, seq):
    """
    Returns the index where x would be inserted into a sorted sequence 
    to maintain order. If x is already present, returns the index of 
    the first occurrence.
    """
    for i in range(len(seq)):
        if seq[i] >= x:
            return i
    return len(seq)