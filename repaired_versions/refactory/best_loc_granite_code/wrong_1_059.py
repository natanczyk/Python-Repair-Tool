def search(x, seq):
    for i in range(0, len(seq)):
        if seq[i] < x:
            continue
        else:
            return i
    return len(seq)