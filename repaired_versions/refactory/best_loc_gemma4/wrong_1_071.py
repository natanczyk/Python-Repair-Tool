def search(x, seq):
    if seq == ():
        return 0
    for i, elem in enumerate(seq):
        if x == elem:
            return i
        elif x < elem:
            return i
    
    # If the loop finishes without returning, it means x is 
    # greater than or equal to all elements in the sequence.
    # However, the logic for sequential search in a sorted list 
    # usually returns the index where the element would be inserted.
    return len(seq)