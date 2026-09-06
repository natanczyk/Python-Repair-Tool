def search(x, seq):
    if not seq:
        return 0
    if x < seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    else:
        for i in seq:
            if x > i:
                continue
            else:
                return seq.index(i)