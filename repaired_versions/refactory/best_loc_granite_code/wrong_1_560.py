def search(x, seq):
    if not seq:
        return 0
    if x > max(seq):
        return len(seq)
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
    return -1