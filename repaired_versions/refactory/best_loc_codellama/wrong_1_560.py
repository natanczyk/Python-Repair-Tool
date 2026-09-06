def search(x, seq):
    if x in seq:
        return seq.index(x)
    else:
        for i in range(len(seq)):
            if seq[i] > x:
                return i
        return len(seq)