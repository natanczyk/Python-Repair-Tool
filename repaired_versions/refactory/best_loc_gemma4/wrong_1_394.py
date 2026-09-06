def search(x, seq):
    n = len(seq)
    if n == 0:
        return 0
    
    # Check if x is smaller than the first element
    if x < seq[0]:
        return 0
    
    # Check if x is larger than the last element
    if x > seq[n-1]:
        return n
        
    # Find the first index i such that x <= seq[i]
    # This handles the case where x is exactly the first element (returns 0)
    # and the case where x falls between two elements.
    for i in range(n):
        if x <= seq[i]:
            return i
            
    return n