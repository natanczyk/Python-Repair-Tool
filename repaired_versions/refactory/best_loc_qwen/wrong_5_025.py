def top_k(lst, k):
    sort = []
    while lst:
        biggest = lst[0]
        for i in lst[1:]:
            if i > biggest:
                biggest = i
        lst.remove(biggest)
        sort.append(biggest)
    
    sort.sort(reverse=True)
    return sort[:k]