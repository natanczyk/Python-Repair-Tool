def top_k(lst, k):
    newlist = []
    while len(newlist) < k:
        biggest = lst[0]
        for i in lst:
            if i > biggest:
                biggest = i
        lst.remove(biggest)
        newlist.append(biggest)
    newlist.sort(reverse=True)
    return newlist