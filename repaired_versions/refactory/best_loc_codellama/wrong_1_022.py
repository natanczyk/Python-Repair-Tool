def search(x, seq):
    lst = list(seq)
    for i in range(len(lst)):
        if x < lst[i]:
            lst.insert(i, x)
            break
    else:
        lst.append(x)
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    return -1