def search(x, seq):
    if seq == []:
        return 0
    for i, v in enumerate(seq):
        if x > v:
            continue
        else:
            return i
    return len(seq)