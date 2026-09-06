def search(x, seq):
    for i, element in enumerate(seq):
        if x > element:
            i += 1
        else:
            return i
    return len(seq)