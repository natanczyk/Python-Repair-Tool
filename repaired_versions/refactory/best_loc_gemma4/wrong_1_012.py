def search(x, seq):
    """
    Returns the index where x would be inserted into the sorted sequence seq 
    to maintain order. If x is already present, returns the index of the first occurrence.
    """
    for i, elem in enumerate(seq):
        if elem >= x:
            return i
    return len(seq)