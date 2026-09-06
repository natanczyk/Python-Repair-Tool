def search(x, seq):
    for i in range(len(seq)):
        if seq[i] >= x:
            break
    else:
        return len(seq)
    return i