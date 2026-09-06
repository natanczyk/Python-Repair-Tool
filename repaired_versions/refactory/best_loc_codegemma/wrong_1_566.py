def search(x, seq):
    for i, elem in enumerate(seq):
        if elem is None:
            return 0
        elif x <= elem:
            return i
        elif i == (len(seq)-1):
            return i+1
        else:
            continue
    if not seq:
        return 0
    return len(seq)