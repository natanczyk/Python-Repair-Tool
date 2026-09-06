def search(x, seq):
    for i in range(0, len(seq)):
        if seq[i] >= x:
            return i
        elif seq[len(seq) - 1] < x:
            return len(seq)
    return len(seq)