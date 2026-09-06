def search(x, seq):
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
    if not seq:
        return 0
    else:
        return len(seq)