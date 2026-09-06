def search(x, seq):
    for i, element in enumerate(seq):
        if element >= x:
            return i
    return len(seq)