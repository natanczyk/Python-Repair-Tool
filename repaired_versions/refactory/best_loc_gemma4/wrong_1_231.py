def search(x, seq):
    if not seq:
        return 0
    
    # The test case search(10, (-5, -1, 3, 5, 7, 10)) == 5 
    # implies that if x is equal to the last element, it should return len(seq) - 1.
    # Therefore, the boundary check for the end must be strictly greater than.
    if x <= seq[0]:
        return 0
    if x > seq[-1]:
        return len(seq)
    
    for i in range(len(seq) - 1):
        if seq[i] <= x <= seq[i+1]:
            return i + 1
            
    return len(seq)