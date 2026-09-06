def search(x, seq):
    if type(seq) == tuple:
        seq = list(seq)
    seq.append(x)
    seq.sort()
    try:
        return seq.index(x)
    except ValueError:
        return 0