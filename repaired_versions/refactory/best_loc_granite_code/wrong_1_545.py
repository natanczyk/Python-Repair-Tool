def search(x, seq):
    if not seq:
        return 0
    else:
        if x < seq[0]:
            return 0
        elif x > seq[-1]:
            return seq.index(seq[-1]) + 1
        else:
            for i in seq:
                if x <= i:
                    return seq.index(i)