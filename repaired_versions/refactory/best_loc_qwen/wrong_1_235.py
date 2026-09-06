def search(x, seq):
    n = len(seq)
    position = 0
    for i in range(n):
        if x > seq[i]:
            position = i + 1
        elif x <= seq[i]:
            return position
    return position