def search(x, seq):
    i = 0
    while i < len(seq) and seq[i] < x:
        i += 1
    return i