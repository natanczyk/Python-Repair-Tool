def search(x, seq):
    n = len(seq)
    if seq == []:
        return 0
    for i in range(0,n):
        currentvalue = seq[i]
        if x <= currentvalue:
            return i
    return n