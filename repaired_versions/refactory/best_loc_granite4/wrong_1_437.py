def search(x, seq):
    if isinstance(seq, tuple):
        for index, value in enumerate(seq):
            if value >= x:
                return index
        return len(seq)

    elif isinstance(seq, list):
        for index, value in enumerate(seq):
            if value >= x:
                return index
        return len(seq)