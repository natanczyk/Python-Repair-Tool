def search(x, seq):
    for i in range(len(seq)):
        if seq[i] < x:
            continue
        elif seq[i] >= x:
            return i
    return len(seq)