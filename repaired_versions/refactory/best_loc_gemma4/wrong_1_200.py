def search(x, seq):
    if not seq:
        return 0
    
    # The original code logic implies it wants to find the index of x
    # or the index where x would be inserted into a sorted sequence.
    # Based on the failing tests search(100, []) == 0 and search(-100, ()) == 0,
    # it seems the function is intended to return the index of x after insertion.
    
    if x in seq:
        return seq.index(x)
    
    for i, elem in enumerate(seq):
        if x < elem:
            return i
            
    return len(seq)