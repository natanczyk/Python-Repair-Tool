def search(x, seq):
    if not seq:
        return 0
    
    # The goal is to find the index where x would be inserted 
    # or the index of the first element >= x in a sorted sequence.
    for i, element in enumerate(seq):
        if x <= element:
            return i
            
    # If x is greater than all elements in the sequence
    return len(seq)