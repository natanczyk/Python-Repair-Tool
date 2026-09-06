def search(x, seq):
    for i in range(len(seq)):
        if not seq:
            return 0
        elif x<=seq[i]:
            return i
    if not seq:
        return 0
    return i+1