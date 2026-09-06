def search(x, seq):
    for index, value in enumerate(seq):
        if x <= value:
            return index
    return len(seq)