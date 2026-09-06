def search(x, seq): 
    if not seq:  # Check if the sequence is empty
        return 0
    
    Index = 0
    if int(x) <= seq[0]:
        return 0
    
    for i in range(len(seq)):
        if int(x) <= seq[i]:
            return i
        Index = i + 1
    
    return Index