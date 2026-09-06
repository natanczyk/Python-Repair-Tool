def search(x, seq):
    if not seq:
        return 0
    if x < seq[0]:
        return 0
    elif x > seq[-1]:
        return len(seq)
    else:
        for j in range(len(seq)):
            if seq[j] == x:
                return j
            if seq[j] > x:
                return j
        return len(seq)