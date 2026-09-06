def search(x, seq):
    if not seq:
        return 0
    if x <= min(seq):
        return 0
    elif x > max(seq):
        return len(seq)
    else:
        for i, item in enumerate(seq):
            if item == x:
                return i
            elif item > x:
                return i