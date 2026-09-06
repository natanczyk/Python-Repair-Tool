def top_k(lst, k):
    lst1 = []
    for i in lst:
        lst1.append(i)
    
    sort = []
    for _ in range(min(k, len(lst1))):
        biggest = lst1[0]
        for element in lst1:
            if element > biggest:
                biggest = element
        lst1.remove(biggest)
        sort.append(biggest)
    
    return sort