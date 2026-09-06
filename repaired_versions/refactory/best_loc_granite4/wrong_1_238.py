def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    
    for index, element in enumerate(seq):
        if x == element:
            return index
        if x < element:
            return index
    
    # If x is greater than all elements in the sequence
    return len(seq)