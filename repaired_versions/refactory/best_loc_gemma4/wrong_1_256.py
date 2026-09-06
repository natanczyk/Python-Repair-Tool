def search(x, seq):
    """
    Returns the index where x should be inserted into the sorted sequence seq 
    to maintain its sorted order (equivalent to bisect_left).
    """
    if not seq:
        return 0
    
    seq = list(seq)
    i = 0
    while i < len(seq):
        if x <= seq[i]:
            return i
        i = i + 1
            
    return len(seq)