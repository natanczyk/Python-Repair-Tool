def search(x, seq):
    if not seq:
        return 0
    if x > seq[-1]:
        return len(seq)
    else:
        for i, val in enumerate(seq):
            if x <= val:
                return i
        return len(seq)