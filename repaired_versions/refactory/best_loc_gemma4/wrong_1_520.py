def search(x, seq):
    """
    Finds the first index where x should be inserted into a sorted sequence 
    to maintain its sorted order.
    """
    for i, elem in enumerate(seq):
        if x <= elem:
            return i
    return len(seq)