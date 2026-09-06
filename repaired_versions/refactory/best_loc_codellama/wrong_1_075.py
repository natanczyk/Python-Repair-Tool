def search(x, seq):
    pos = 0
    for i in range(len(seq)):
        if x <= seq[i]:
            pos = i
            break
    else:
        pos = len(seq)
    return pos