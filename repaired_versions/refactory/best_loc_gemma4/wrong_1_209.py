def search(x, seq):
    if not seq:
        return 0
    if x < seq[0]:
        return 0
    if x > seq[-1]:
        return len(seq)
    
    for i in range(len(seq)):
        if seq[i] == x:
            return i
        if i < len(seq) - 1 and seq[i] < x < seq[i+1]:
            return i + 1
    return len(seq)