def search(x, seq):
    seq = list(seq)
    for i, elem in enumerate(seq):
        if x == elem:
            return i
    # If not found, insert x at the correct sorted position
    seq.append(x)
    seq.sort()
    return seq.index(x)