def search(x, seq):
    if type(seq) == tuple:
        seq = list(seq)
        seq.append(x)
        seq.sort()
        return seq.index(x)
    else:
        seq.append(x)
        seq.sort()
        return seq.index(x)