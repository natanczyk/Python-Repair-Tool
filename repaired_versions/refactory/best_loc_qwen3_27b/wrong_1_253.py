def search(x, seq):
    if seq == [] or seq == ():
        return 0
    if x <= seq[0]:
        return 0
    if x > seq[len(seq) - 1]:
        return len(seq)
    for i in range(1, len(seq)):
        if x <= seq[i] and x > seq[i-1]:
            return i
    return len(seq)