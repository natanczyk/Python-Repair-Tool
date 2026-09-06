def search(x, seq):
    if not seq:
        return 0
    position = enumerate(seq)
    for i in seq:
        if x <= i:
            for index in position:
                if index[1] == i:
                    return index[0]
    return len(seq)