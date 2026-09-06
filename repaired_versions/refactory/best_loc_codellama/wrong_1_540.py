def search(x, seq):
    if not seq:
        return 0
    for i in range(len(seq)):
        if seq[i] >= x:
            break
    else:
        return len(seq)
    return i