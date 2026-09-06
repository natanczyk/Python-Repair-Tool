def search(x, seq):
    
    seq = list(seq)
    if not seq:
        seq.append(x)
        return 0
    
    for i, elem in enumerate(seq):
        if x <= elem:
            seq.insert(i, x)
            return i
    seq.append(x)
    return len(seq) - 1