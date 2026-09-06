def search(x, seq):
    if len(seq) == 0:
        return 0
    for i in range(len(seq)):
        if seq[i] >= x:
            return i
    return len(seq)