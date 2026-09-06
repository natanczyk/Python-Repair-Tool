def search(x,seq):
    if not seq:
        return 0
    if max(seq) < x:
        return len(seq)
    if x <= min(seq):
        return 0
    for i in range(len(seq)):
        if seq[i] >= x:
            return i
    return len(seq)