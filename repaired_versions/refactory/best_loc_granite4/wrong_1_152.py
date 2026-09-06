def search(x, seq):
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
    if seq and seq[-1] < x:
        return len(seq)
    return 0