def search(x, seq):
    """
    Returns the index where x would be inserted into the sorted sequence seq
    to maintain its sorted order.
    """
    for i, element in enumerate(seq):
        if x <= element:
            return i
    return len(seq)