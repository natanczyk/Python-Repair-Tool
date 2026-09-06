def search(x, seq):
    """
    Returns the number of elements in the sorted sequence 'seq' 
    that are strictly less than 'x'.
    """
    if not seq:
        return 0
    
    count = 0
    for item in seq:
        if item < x:
            count += 1
        else:
            break
    return count