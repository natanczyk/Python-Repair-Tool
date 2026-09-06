def search(x, seq):
    for index, item in enumerate(seq):
        if x <= item:
            return index
    return len(seq)