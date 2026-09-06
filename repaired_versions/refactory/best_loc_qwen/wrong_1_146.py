def search(x, seq):
    seq = list(seq)
    
    if len(seq) == 0:
        return 0
    
    for i in range(len(seq)):
        if seq[i] == x:
            return i
        elif seq[i] > x:
            return i
    
    return len(seq)  # Return the insertion point if x is not found