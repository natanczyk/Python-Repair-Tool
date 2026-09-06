def search(x, seq):
    seq = list(seq)
    seq.sort()
    for i in range(len(seq)):
        if seq[i] == x:
            return i
        elif seq[i] > x:
            return i
    return len(seq)