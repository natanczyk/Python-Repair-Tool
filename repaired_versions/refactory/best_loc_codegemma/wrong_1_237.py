def search(x, seq):
    if not seq:
        return 0
    if x <= seq[-1]:
        for i in range(len(seq)):
            if seq[i] < x:
                continue
            else:
                return i
    else:
        return len(seq)