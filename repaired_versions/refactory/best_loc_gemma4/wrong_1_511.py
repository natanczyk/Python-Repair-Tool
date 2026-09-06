def search(x, seq):
    if not seq:
        return 0
    for i in seq:
        if x < i:
            return seq.index(i)
        elif x == i:
            return seq.index(i)
    
    if x > seq[-1]:
        return len(seq)
    
    return 0