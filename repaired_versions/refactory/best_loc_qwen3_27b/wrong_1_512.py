def search(x, seq): 
    # Handle empty sequence
    if len(seq) == 0:
        return 0
    
    # Check if x is less than the first element
    if int(x) < seq[0]:
        return 0
    
    # Check if x is greater than the last element
    if int(x) > seq[len(seq)-1]:
        return len(seq)
    
    # Sequential search through the sequence
    for i in range(len(seq)):
        if int(x) <= seq[i]:
            return i
    
    # If not found, return the length of the sequence
    return len(seq)