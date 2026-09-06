def search(x, seq):
    """
    Perform a search that returns the index of the first element 
    greater than or equal to x (the insertion point).
    """
    for i in range(len(seq)):
        if seq[i] >= x:
            return i
    return len(seq)