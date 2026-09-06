def search(x, seq):
    if len(seq) == 0:
        return 0
    if seq[0] >= x:
        return 0
    for i in range(len(seq)-1):
        if seq[i] < x and seq[i+1] >= x:
            return i+1
    return len(seq)