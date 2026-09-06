def search(x, seq):
    if not seq:
        return len(seq)
    if x <= seq[0]:
        return 0
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
    return len(seq)