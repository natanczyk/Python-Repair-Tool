def top_k(lst, k):
    af_sort = []
    lst = lst.copy()  # Avoid modifying the original list
    while lst:
        biggest = lst[0]
        for element in lst:
            if element > biggest:
                biggest = element
        lst.remove(biggest)
        af_sort.append(biggest)
    return af_sort[0:k]