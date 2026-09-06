def search(x, seq):
    """
    Finds the index of the first element in a sorted sequence that is 
    greater than or equal to x.
    """
    if not seq: 
        return 0
    
    # The goal is to find the index i such that seq[i] >= x.
    # If no such element exists, return len(seq).
    for i in range(len(seq)):
        if seq[i] >= x:
            return i
            
    return len(seq)