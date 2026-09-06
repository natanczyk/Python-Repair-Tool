def search(x, seq):
    if not seq:
        return 0
    for i, elem in enumerate(seq):
        if x > elem:
            continue
        else:
            return i
    return len(seq)