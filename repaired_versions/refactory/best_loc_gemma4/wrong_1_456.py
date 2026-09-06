def search(x, seq):
    """
    Returns the number of elements in the sorted sequence 'seq' that are strictly less than 'x'.
    This is equivalent to finding the insertion point for x to maintain sorted order (bisect_left).
    """
    count = 0
    for item in seq:
        if item < x:
            count += 1
        else:
            break
    return count