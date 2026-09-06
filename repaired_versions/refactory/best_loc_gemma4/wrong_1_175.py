def search(x, seq):
    if not seq:
        return 0
    
    # Convert to list to handle indexing and max() efficiently
    seq_list = list(seq)
    
    # If x is greater than the maximum element, return the index after the max element
    if x > max(seq_list):
        return len(seq_list)
    
    # Find the index of the first element that is greater than or equal to x
    for i, element in enumerate(seq_list):
        if x <= element:
            return i
            
    return len(seq_list)