def search(x, seq):
    if seq == []:
        return 0
    if x < 0:
        return 0
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
    return len(seq)