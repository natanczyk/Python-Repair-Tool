def search(x, seq):
    pos = len(seq)
    for i in range(len(seq)):
        if x <= seq[i]:
            pos = i
            break
    return pos