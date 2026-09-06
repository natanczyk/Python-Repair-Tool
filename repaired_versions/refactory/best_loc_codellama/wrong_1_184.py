def search(x, seq):
    for i, item in enumerate(seq):
        if item == x:
            return i
        elif item > x:
            return i
    return len(seq)