def search(x, seq):
    for i in range(len(seq)):
        if seq[i] >= x:
            return i
    if len(seq) > 0 and seq[len(seq) - 1] < x:
        return len(seq)
    return 0