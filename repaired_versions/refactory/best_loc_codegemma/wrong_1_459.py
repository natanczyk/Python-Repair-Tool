def search(x, seq):
    for i in range(len(seq)):
        if seq[i] >= x:
            return i
        elif i == len(seq) - 1:
            return len(seq)
    return 0