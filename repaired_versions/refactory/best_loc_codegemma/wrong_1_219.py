def search(x, seq):
    if not seq:
        return 0
    for i, elem in enumerate(seq):
        if x <= elem:
            return i
        elif i == len(seq) - 1 and x > elem:
            return i + 1