def search(x, seq):
    if not seq:
        return 0
    
    # If x is smaller than or equal to the first element, it's at position 0
    if x <= seq[0]:
        return 0
    
    # Iterate through the sequence to find the insertion point
    for i in range(len(seq) - 1):
        if seq[i] < x <= seq[i+1]:
            return i + 1
            
    # If x is greater than the last element, it's at the end of the sequence
    if x > seq[-1]:
        return len(seq)
    
    # This part handles cases where x is exactly the last element 
    # but not caught by the loop (though the loop logic covers most)
    return len(seq)