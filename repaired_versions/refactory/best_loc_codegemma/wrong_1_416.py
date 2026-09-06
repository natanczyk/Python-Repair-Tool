def search(x, seq):
    for i, elem in enumerate(seq) :
        if x <= elem :
            return i
    if not seq:
        return 0
    return len(seq)