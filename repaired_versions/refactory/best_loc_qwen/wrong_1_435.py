def search(x, seq):
    counter = 0
    for i, elem in enumerate(seq):
        if x <= elem:
            return counter
        else:
            counter = i + 1
    return counter