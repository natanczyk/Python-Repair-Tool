def search(x, seq):
    lst1 = list(seq)
    if len(lst1) == 0:
        return 0
    else:
        length = len(lst1)
        if x < lst1[0]:
            return 0
        for i in range(length):
            if lst1[i] >= x:
                return i
        return length