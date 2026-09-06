def search(x, seq):
    if not seq:
        return 0
    for i, element in enumerate(seq):
        if x <= element:
            return i
        elif x > max(seq):
            return len(seq)
    return -1