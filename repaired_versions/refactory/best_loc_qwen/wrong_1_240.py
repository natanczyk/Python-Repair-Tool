def search(x, seq):
    n = len(seq)
    for i in range(n):
        currentvalue = seq[i]
        if x > currentvalue:
            continue
        elif x <= currentvalue:
            return i
    return n