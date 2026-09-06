def search(x, seq):
    l = len(seq)
    if l == 0:
        return 0
    if x <= seq[0]:
        return 0
    if x > seq[l-1]:
        return l
    if x == seq[l-1]:
        return l-1
    
    for i in range(l - 1):
        if x >= seq[i] and x <= seq[i+1]:
            return i + 1
    return l