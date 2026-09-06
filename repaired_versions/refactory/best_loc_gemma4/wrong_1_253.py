def search(x, seq):
    if not seq:
        return 0
    
    # Handle cases where x is smaller than or equal to the first element
    if x <= seq[0]:
        return 0
    
    # Handle cases where x is larger than the last element
    if x > seq[-1]:
        return len(seq)
    
    # Search for the position where x fits in the sorted sequence
    # We start from index 1 because index 0 is handled above
    for i in range(1, len(seq)):
        if x <= seq[i] and x > seq[i-1]:
            return i
            
    return len(seq)