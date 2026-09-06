def search(x, seq):
    for i in range(len(seq)):
        if x <= seq[i] and (i == 0 or x >= seq[i-1]):
            return i
    return len(seq)