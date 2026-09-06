def search(x, seq):
    for i, ele in enumerate(seq):
        if x > ele:
            continue
        else:
            return i
    return len(seq)