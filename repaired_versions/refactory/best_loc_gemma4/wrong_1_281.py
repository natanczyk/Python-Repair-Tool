def search(x, seq):
    if not seq:
        return 0
    
    # If x is less than or equal to the first element, it's at index 0
    if x <= seq[0]:
        return 0
    
    # Check intervals between elements
    for i in range(len(seq) - 1):
        if seq[i] < x <= seq[i+1]:
            return i + 1
            
    # If x is greater than the last element
    if x > seq[-1]:
        return len(seq)
    
    # Fallback for cases where x is within the range of the sequence 
    # but not caught by the loop (though the logic above covers it)
    return len(seq)