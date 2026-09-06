def search(x, seq):
    position = 0
    for ele in seq:
        if x <= ele:
            break
        position += 1
    return position if position < len(seq) else len(seq)