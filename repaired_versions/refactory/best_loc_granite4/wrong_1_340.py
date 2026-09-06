def search(x, seq):
    for counter, value in enumerate(seq):
        if x <= value:
            return counter
    return len(seq)