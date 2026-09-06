def search(x, seq):
    """
    Sequential search for the index of x in seq.
    If x is not found, it returns the index where x would be inserted 
    to maintain a sorted order (assuming seq is sorted).
    """
    seq = list(seq)
    for i, elem in enumerate(seq):
        if elem == x:
            return i
        if elem > x:
            return i
    return len(seq)