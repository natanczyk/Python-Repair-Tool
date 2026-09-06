def search(x, seq):
    if not seq:
        return 0
    if x < seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    for i, elem in enumerate(seq):
        if elem == x:
            return i
        elif elem > x:
            return i
    return len(seq)