def search(x, seq):
    if len(seq) == 0:
        return 0
    elif x in seq:
        return seq.index(x)
    else:
        for i, elem in enumerate(seq):
            if elem >= x:
                return i
    return len(seq)