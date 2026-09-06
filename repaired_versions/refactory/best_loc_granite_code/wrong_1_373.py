def search(x, seq):
    for i in range(len(seq)):
        if seq[i] < x:
            continue
        else:
            return i
    return len(seq)