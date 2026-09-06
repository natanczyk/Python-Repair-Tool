def search(x, seq):
    if not seq:
        return 0
    
    max_val = max(seq)
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
        elif x > max_val:
            return len(seq)