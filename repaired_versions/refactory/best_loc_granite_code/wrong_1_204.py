def search(x, seq):
    l = len(seq)
    if len(seq) == 0:
        return 0
    elif x <= seq[0]:
        return 0
    elif x > seq[l - 1]:
        return l
    else:
        for i in range(l - 1):
            if x >= seq[i] and x <= seq[i + 1]:
                return i + 1
            else:
                continue