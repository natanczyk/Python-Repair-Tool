def search(x, seq):
    if len(seq) == 0:
        return False
    for i in range(len(seq)):
        if x < seq[i]:
            return i
        elif x == seq[i]:
            return i
    return len(seq)