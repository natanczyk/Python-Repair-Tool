def search(x, seq):
    y = len(seq)
    if y == 0:
        return 0
    else:
        for i in range(y):
            if x <= seq[i]:
                return i
        return y