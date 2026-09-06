def search(x, seq):
    length = len(seq)
    for i, elem in enumerate(seq):
        if x <= elem:
            return i
    return length