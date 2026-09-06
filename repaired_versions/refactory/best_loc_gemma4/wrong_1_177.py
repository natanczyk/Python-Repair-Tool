def search(x, seq):
    if not seq:
        return 0
    
    # Convert to list once to avoid repeated conversions
    seq_list = list(seq)
    
    for i, element in enumerate(seq_list):
        if x <= element:
            return i
            
    # If x is greater than all elements in the sequence, 
    # return the index after the last element.
    return len(seq_list)