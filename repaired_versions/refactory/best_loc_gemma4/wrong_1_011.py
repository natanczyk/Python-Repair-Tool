def search(x, seq):
    last_idx = 0
    for i, elem in enumerate(seq):
        if elem < x:
            last_idx = i + 1
    return last_idx