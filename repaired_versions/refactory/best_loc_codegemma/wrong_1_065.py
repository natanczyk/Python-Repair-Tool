def search(x, seq):
    for i in range(0,len(seq)):
        if x == seq[i]:
            return i
        elif x < seq[i]:
            return i
    return len(seq)