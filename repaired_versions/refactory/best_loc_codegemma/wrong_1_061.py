def search(x, seq):
    if len(seq) == 0:
        return 0
    for i in seq:
        if x <= i:
            return seq.index(i)
    return len(seq)