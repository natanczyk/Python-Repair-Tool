def search(x, seq):
    l = len(seq)
    for i in range(l):
        if i == l:
            break
        if x <= seq[i]:
            break
    else:
        i = l
    return i