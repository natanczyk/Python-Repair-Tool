def top_k(lst, k):
    x = []
    for i in range(k):
        y = lst[0]
        for j in lst:
            if y < j:
                y = j
        x.append(y)
        lst.remove(y)
    return x