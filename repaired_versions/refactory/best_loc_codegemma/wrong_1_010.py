def search(x, seq):
    for i, elem in enumerate(seq):
        if x == elem:
            return i
        elif x > elem:
            continue
        else:
            return i
    return len(seq)