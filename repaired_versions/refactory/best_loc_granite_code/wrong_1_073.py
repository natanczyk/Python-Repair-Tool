def search(x, seq):
    for i in range(len(seq)):
        if x <= seq[i]:
            a = i
            break
    else:
        a = len(seq)
    return a