def search(x, seq): 
    # Handle empty sequence case
    if not seq:
        return 0
    
    # Convert x to integer for comparison
    x_val = int(x)
    
    # Sequential search to find the first index where seq[i] >= x
    for i in range(len(seq)):
        if seq[i] >= x_val:
            return i
            
    # If x is greater than all elements in the sequence
    return len(seq)