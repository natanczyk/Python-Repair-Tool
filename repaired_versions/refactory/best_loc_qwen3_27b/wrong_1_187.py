def search(x, seq):
    if not seq:
        return 0
    
    # Find the first index where seq[i] >= x
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
    
    # If x is greater than all elements, return len(seq)
    return len(seq)