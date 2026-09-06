def search(x, seq):
    for i in range(0, len(seq)):
        if seq[i] < x:
            continue
        elif seq[i] >= x:
            return i
    return len(seq)