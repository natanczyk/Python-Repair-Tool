def search(x, seq):
    if not seq:
        return 0
    for element in seq:
        if x <= element:
            return seq.index(element)
    if x >= max(seq):
        return len(seq)
    return -1