def search(x, seq):
    for i in range(len(seq)):
        if seq[i] >= x:
            break
    else:
        i = len(seq)
    return i