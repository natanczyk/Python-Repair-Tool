def search(x, seq):
    l = len(seq)
    for i in range(l + 1):
        if i == l or x <= seq[i]:
            break
    return i