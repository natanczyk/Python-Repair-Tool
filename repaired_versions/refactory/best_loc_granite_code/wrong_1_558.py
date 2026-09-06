def search(x, seq):
    pos = 0
    for i, elem in enumerate(seq):
        if elem < x:
            pos = i + 1
        elif elem == x:
            pos = i
            break
    return pos