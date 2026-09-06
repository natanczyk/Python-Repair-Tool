def search(x, seq):
    for i, item in enumerate(seq):
        if x <= item:  # Change from < to <= to include equal values
            return i
    return len(seq)