def search(x, seq):
    i = 0
    for i, ele in enumerate(seq, 0):
        if x > ele:
            continue
        else:
            return i
    return i if not seq else i + 1 if x > seq[-1] else i