def search(x, seq):
    for i in seq:
        if x <= i:
            return seq.index(i)
    
    if not seq:
        return 0
    elif x > max(seq):
        return len(seq)
    
    return len(seq)