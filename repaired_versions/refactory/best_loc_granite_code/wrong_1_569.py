def search(x, seq):
    position = -1
    for elem in seq:
        if x <= elem:
            break
        position += 1
    return position + 1