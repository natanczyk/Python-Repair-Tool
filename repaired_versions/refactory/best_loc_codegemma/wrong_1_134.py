def search(x, seq):
    if not seq:
        return 0
    for i, elem in enumerate(seq):
        if i == 0 and x < elem:
            return 0
        elif x == elem:
            return i
        elif x < elem:
            return i
        elif x > seq[-1]:
            return len(seq)