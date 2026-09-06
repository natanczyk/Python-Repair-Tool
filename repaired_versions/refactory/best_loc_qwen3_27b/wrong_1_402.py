def search(x, seq):
    if not seq:
        return 0
    for i, elem in enumerate(seq):
        if x > elem and i < (len(seq)-1):
            continue
        elif x <= elem:
            return i
        else:
            return len(seq)
    return len(seq)