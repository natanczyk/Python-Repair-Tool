def top_k(lst, k):
    newlst = []
    for i in range(k):
        maximum = lst[0]
        for j in lst:
            if j > maximum:
                maximum = j
        newlst.append(maximum)
        lst.remove(maximum)
    return newlst