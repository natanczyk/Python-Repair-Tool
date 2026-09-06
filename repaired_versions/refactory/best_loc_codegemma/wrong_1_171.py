def search(x, seq):
    if not seq:
        return 0
    elif x in seq:
        return list(seq).index(x)
    elif x > max(seq):
        return len(seq)
    else:
        for element in seq:
            if x <= element:
                return list(seq).index(element)
        return -1