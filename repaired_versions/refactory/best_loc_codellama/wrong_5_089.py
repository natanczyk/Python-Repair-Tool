def top_k(lst, k):
    newlist = []
    while lst:
        biggest = lst[0]
        for i in lst:
            if i > biggest:
                biggest = i
        lst.remove(biggest)
        newlist.append(biggest)
    return newlist[:k]