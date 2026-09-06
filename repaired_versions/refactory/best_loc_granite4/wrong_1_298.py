def search(x, seq):
    for i, value in enumerate(seq):
        if x > value:
            continue
        else:
            return i
    return len(seq)