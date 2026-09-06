def search(x, seq):
    i = 0
    for i in range(len(seq)):
        if x <= seq[i]:
            break
    else:
        i = len(seq)
    return i