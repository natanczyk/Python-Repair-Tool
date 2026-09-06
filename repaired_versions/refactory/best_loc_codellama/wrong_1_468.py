def search(x, seq):
    if not seq:
        return 0
    if x < seq[0]:
        return 0
    i = 0
    while i < len(seq):
        if x <= seq[i]:
            return i
        i += 1
    return len(seq)