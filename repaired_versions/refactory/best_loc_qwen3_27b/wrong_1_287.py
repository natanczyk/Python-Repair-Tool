def search(x, seq):
    if seq is () or len(seq) == 0:
        return 0
    if x < seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    else:
        for i in range(len(seq)):
            if x == seq[i]:
                return i
            elif x > seq[i] and (i + 1 < len(seq) and x < seq[i + 1]):
                return i + 1
        return len(seq)