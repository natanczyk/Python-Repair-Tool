def search(x, seq):
    lst1 = list(seq)
    if len(lst1) == 0:
        return 0
    length = len(lst1)
    lst2 = []
    if x < lst1[0]:
        lst2 = [x] + lst1
    elif x > lst1[length -1]:
        lst2 = lst1 + [x]
    else:
        for i in range(0, length - 1):
            if lst1[i] <= x <= lst1[i+1]:
                lst2 = lst1[:i+1] + [x] + lst1[i+1:]
    if lst2:
        return lst2.index(x)
    else:
        return 0