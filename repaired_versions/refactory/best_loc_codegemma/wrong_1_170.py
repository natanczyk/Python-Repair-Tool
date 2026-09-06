def search(x, seq):
    for element in seq:
        if x <= element:
            return list(seq).index(element)
        elif x > max(seq):
            return len(seq)
    if not seq:
        return 0