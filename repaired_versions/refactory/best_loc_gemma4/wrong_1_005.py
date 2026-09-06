def search(x, seq):
    if not seq:
        return 0
    
    # The goal of a sequential search for the first occurrence of x 
    # (or the position where x would be inserted in a sorted list)
    # is to find the index of the first element that is >= x.
    for i in range(len(seq)):
        if seq[i] >= x:
            return i
            
    return len(seq)