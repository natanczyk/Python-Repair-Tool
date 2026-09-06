def search(x, seq):
    if not seq:
        return 0
    
    # Handle the case where x is less than or equal to the first element
    if x <= seq[0]:
        return 0
    
    # Search for the first index i where x <= seq[i]
    # Since we already checked seq[0], we start from index 1
    for i in range(1, len(seq)):
        if x <= seq[i]:
            return i
            
    # If x is greater than all elements in the sequence
    return len(seq)