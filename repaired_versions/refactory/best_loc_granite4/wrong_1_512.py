def search(x, seq):
    x = int(x)
    if not seq:
        return 0
    if x <= seq[0]:
        return 0
    if x > seq[-1]:
        return len(seq)
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
    return len(seq)