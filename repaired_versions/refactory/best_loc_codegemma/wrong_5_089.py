def top_k(lst, k):
    newlist = []
    while lst and len(newlist) < k:
        biggest = lst[0]
        for i in lst:
            if i > biggest:
                biggest = i
            else:
                continue
        lst.remove(biggest)
        newlist.append(biggest)
    return newlist