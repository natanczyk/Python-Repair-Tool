def search(x, seq):
    for i, val in enumerate(seq):
        if x > val:
            continue
        else:
            return i
    return len(seq)