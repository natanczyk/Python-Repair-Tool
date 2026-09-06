def search(x, seq):
    for i in range(len(seq)):
        if seq[i]>=x:
            break
        elif i == len(seq) - 1:
            return len(seq)
    if not seq:
        return 0
    return i