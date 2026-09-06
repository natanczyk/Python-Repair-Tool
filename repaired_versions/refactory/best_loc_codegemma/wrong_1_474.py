def search(x, seq):
    if not seq:
        return 0
    for i, element in enumerate(seq):
        if x <= element:
            return i
        i += 1
    return len(seq)