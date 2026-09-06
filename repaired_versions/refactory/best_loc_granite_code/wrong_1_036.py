def search(x, seq):
    if not seq:
        return 0
    for i in range(len(seq)):
        if seq[i] == x:
            return i
        elif seq[i] > x:
            return i
    return len(seq)