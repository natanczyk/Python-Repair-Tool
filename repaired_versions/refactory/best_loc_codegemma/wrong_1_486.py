def search(x, seq):
    result = len(seq)
    for i in range(len(seq)):
        if seq[i] >= x:
            result = i
            break
    return result