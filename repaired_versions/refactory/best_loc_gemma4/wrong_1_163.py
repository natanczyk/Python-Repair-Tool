def search(x, seq):
    if not seq:
        return 0
    
    # If x is less than or equal to the first element, it's at index 0
    if x <= seq[0]:
        return 0
    
    # If x is greater than the last element, it's at index len(seq)
    if x > seq[-1]:
        return len(seq)
    
    # Check intervals between elements
    # We want the index i such that seq[i-1] < x <= seq[i]
    for i in range(1, len(seq)):
        if seq[i-1] < x <= seq[i]:
            return i
            
    return len(seq)