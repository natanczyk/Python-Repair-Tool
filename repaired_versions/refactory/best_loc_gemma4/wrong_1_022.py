def search(x, seq):
    lst = list(seq)
    for i in range(len(lst)):
        if lst[i] >= x:
            return i
    return len(lst)