def search(x, seq):
    if len(seq) == 0:
        return 0
    for i, elem in enumerate(seq):
        if i == 0 and x < elem:
            return 0
        elif x <= elem:
            return i
        elif i == len(seq) - 1:
            return len(seq)