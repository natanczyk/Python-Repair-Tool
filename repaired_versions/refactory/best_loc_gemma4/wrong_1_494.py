def search(x, seq):
    if not seq:
        return 0
    for i, elem in enumerate(seq):
        if x <= elem:
            return i
    if x > seq[-1]:
        return len(seq)
    return len(seq)