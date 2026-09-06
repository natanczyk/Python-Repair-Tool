def search(x, seq):
    if isinstance(seq, tuple):
        seq = list(seq)
    seq.append(x)
    seq.sort()
    return seq.index(x)