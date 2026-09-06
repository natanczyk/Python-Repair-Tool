def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    
    for count, ele in enumerate(seq):
        if x <= ele:
            return count
    
    return len(seq)