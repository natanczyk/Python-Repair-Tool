def search(x, seq):
    if len(seq) == 0:
        return 0
    if len(seq) == 1:
        if x <= seq[0]:
            return 0
        else:
            return 1
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
    return len(seq)