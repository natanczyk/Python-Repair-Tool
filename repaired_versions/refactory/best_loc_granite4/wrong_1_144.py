def search(x, seq):
    seq = list(seq)
    for index, value in enumerate(seq):
        if value >= x:
            return index
    return len(seq)