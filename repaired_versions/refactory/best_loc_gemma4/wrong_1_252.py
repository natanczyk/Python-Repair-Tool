def search(x, seq):
    if not seq:
        return 0
    
    # If x is less than or equal to the first element, it belongs at index 0
    if x <= seq[0]:
        return 0
    
    # If x is greater than the last element, it belongs at the end
    if x > seq[-1]:
        return len(seq)
    
    # Search for the first index i where x <= seq[i]
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
            
    return len(seq)