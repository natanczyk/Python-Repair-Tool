def search(x, seq):
    if type(seq) == tuple:
        seq = list(seq)
        seq.append(x)
    elif type(seq) == list:
        seq.append(x)
    a = sorted(seq)
    return a.index(x)