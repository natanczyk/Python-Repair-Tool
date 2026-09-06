def search(x, seq):
    lst = list(seq)
    for i, val in enumerate(lst):
        if x <= val:
            return i
    return len(lst)