def search(x, seq):
    counter = -1
    for i, elem in enumerate(seq):
        if x <= elem:
            counter = i
            break
    if counter == -1:
        counter = len(seq)
    return counter