def search(x, seq):
    lst = list(seq)
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    for i in range(len(lst)):
        if x < lst[i]:
            lst.insert(i,x)
            return i
    lst.append(x)
    return len(lst) - 1