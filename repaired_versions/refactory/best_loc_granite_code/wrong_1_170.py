def search(x, seq):
    if not seq:
        return 0
    for element in seq:
        if x <= element:
            return list(seq).index(element)
    return list(seq).index(max(seq)) + 1