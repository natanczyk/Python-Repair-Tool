def top_k(lst, k):
    sort = []
    while lst and k > 0: 
        biggest = lst[0]
        for element in lst:
            if element > biggest:
                biggest = element
                
        lst.remove(biggest)
        sort.append(biggest)
        k -= 1
    return sort