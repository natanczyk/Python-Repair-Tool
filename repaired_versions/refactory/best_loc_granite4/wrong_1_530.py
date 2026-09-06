def search(x, seq):
    length = len(seq)
    if length == 0:
        return 0
    for i, elem in enumerate(seq):
        if x <= elem:
            return i
        elif i == length - 1:
            return length