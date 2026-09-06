def search(x, seq):
    n = len(seq)
    position = 0
    for i in range(0, n):
        currentvalue = seq[i]
        if x > currentvalue:
            position = i + 1
        else:
            return i
    return position