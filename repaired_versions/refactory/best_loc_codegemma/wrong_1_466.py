def search(x, seq):
    if not seq:
        return 0
    elif x < seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    else:
        for i, value in enumerate(seq):
            if x == value:
                return i
            elif seq[i] <= x <= seq[i + 1]:
                return i + 1