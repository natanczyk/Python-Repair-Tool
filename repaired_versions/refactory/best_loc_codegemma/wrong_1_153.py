def search(x, seq):
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
    if not seq:
        return 0
    return len(seq)