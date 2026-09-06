def search(x, seq):
    if not seq:  # Handles both empty lists and empty tuples
        return 0    
    if x <= seq[0]:
        return 0
    for i in range(len(seq)-1):
        if seq[i+1] >= x and x > seq[i]:
            return i+1
    return len(seq)