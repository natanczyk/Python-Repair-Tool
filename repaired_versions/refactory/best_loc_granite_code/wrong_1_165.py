def search(x, seq):
    for i in range(len(seq)):
        if x <= seq[i]:
            break
    else:
        i = len(seq)
    return i