def top_k(lst, k):
    af_sort = []
    while lst:
        biggest = lst[0] 
        for element in lst:
            if element > biggest:
                biggest = element
        af_sort.append(biggest)
        lst.remove(biggest)
    return af_sort[0:k]