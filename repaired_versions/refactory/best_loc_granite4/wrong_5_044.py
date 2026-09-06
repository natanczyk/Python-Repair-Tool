def top_k(lst, k):
    af_sort = []
    while lst and len(af_sort) < k:
        biggest = lst[0] 
        for element in lst:
            if element > biggest:
                biggest = element
        lst.remove(biggest)
        af_sort.append(biggest)
    return af_sort