def search(x, seq):
    for i in range(len(seq)):
        if seq[i] < x:
            continue
        return i
    return len(seq)