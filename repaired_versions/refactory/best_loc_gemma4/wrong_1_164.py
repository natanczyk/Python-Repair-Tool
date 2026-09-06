def search(x, seq):
    if len(seq) == 0:
        return 0
    
    # If x is less than or equal to the first element, it belongs at index 0
    if x <= seq[0]:
        return 0
    
    # If x is greater than the last element, it belongs at the end
    if x > seq[-1]:
        return len(seq)
    
    # Find the index i such that seq[i-1] < x <= seq[i]
    for i in range(1, len(seq)):
        if x <= seq[i]:
            return i
            
    return len(seq)