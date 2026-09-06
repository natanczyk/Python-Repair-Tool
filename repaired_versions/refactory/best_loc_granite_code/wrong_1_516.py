def search(x, seq):
    if len(seq) == 0:
        return 0
    if x > seq[-1]:
        return len(seq)
    else:
        for i in range(len(seq)):
            if x > seq[i]:
                continue
            else:
                return i