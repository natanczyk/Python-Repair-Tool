def search(x, seq):
    lst1 = list(seq)
    length = len(lst1)
    lst2 = []
    if length == 0:
        lst2 = [x]
    elif x < seq[0]:
        lst2 = [x] + lst1
    elif x > seq[length - 1]:
        lst2 = lst1 + [x]
    else:
        for i in range(length - 1):
            if seq[i] <= x <= seq[i + 1]:
                lst2 = lst1[:i + 1] + [x] + lst1[i + 1:]
                break
    lst2 = lst2 + [x] if x not in lst2 else lst2
    print(lst2)
    for i in range(len(lst2)):
        if x == lst2[i]:
            return i