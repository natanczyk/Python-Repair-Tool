def search(x, seq):
    if x not in seq:
        for i, elem in enumerate(seq):
            if x <= elem:
                return i
        return len(seq)
    elif x > seq[len(seq) - 1]:
        return len(seq)
    else:
        for i, elem in enumerate(seq):
            if x <= elem:
                return i
        return len(seq)