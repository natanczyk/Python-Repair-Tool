def search(x, seq):
    if not seq:
        return 0
    if max(seq) < x:
        return len(seq)
    if x <= min(seq):
        return 0
    for i, value in enumerate(seq):
        if value >= x:
            return i