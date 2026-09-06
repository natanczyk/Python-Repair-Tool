def search(x, seq):
    if not seq:
        return 0
    for element in seq:
        if x <= element:
            return list(seq).index(element)
        elif x > max(seq):
            return len(seq)
    return -1