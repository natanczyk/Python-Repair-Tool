def search(x, seq):
    counter = 0
    for i, elem in enumerate(seq):
        if x <= elem:
            counter = i
            break
    else:
        counter = len(seq)
    return counter