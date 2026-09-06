def search(x, seq):
    for i,elem in enumerate(seq):
        if x > elem:
            continue
        return i
    if not seq:
        return 0
    return len(seq)