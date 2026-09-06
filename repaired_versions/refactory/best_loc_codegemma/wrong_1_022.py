def search(x, seq):
    lst = list(seq)
    for i in range(len(lst)):
        if x < lst[i]:
            lst.insert(i,x)
            break
        else:
            lst.insert(len(lst),x)
    for i in range(len(lst)):
         if lst[i] == x:
             return i
    if x not in lst:
        lst.insert(len(lst), x)
    return len(lst) - 1