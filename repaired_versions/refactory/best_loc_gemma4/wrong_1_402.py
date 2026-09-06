def search(x, seq):
    for i, elem in enumerate(seq):
        if x > elem:
            continue
        elif x <= elem:
            return i
    return len(seq)