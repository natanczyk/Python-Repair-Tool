def search(x, seq):
    if x not in seq:
        for i, elem in enumerate(seq):
            if x <= elem:
                return i
        return len(seq)
    else:
        return seq.index(x)