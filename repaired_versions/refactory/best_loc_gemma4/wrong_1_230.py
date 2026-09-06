def search(x, seq):
    if not seq:
        return 0
    if x <= seq[0]:
        return 0
    if x > seq[-1]:
        return len(seq)
    
    for i in range(len(seq) - 1):
        if seq[i] <= x <= seq[i+1]:
            return i + 1
    return len(seq)