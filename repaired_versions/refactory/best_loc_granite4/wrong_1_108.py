def search(x, seq):
    if len(seq) == 0:
        return 0
    elif x < seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    else:
        for index, i in enumerate(seq):
            if x <= i:
                return index
        return None