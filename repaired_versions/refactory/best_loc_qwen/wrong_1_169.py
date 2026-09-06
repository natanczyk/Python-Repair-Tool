def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    
    for i, element in enumerate(seq):
        if x <= element:
            return i
    
    return len(seq)  # x is greater than all elements in the sequence