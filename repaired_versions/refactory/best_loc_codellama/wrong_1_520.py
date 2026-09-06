def search(x, seq):
    if x in seq:
        for i, elem in enumerate(seq):
            if x == elem:
                return i
    else:
        for i, elem in enumerate(seq):
            if x < elem:
                return i
        return len(seq)