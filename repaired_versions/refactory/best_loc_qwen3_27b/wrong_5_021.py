def top_k(lst, k):
    r = []
    # Make a copy to avoid modifying the original list
    lst_copy = lst[:]
    for _ in range(0, k):
        biggest = lst_copy[0]
        for item in lst_copy:
            if biggest < item:
                biggest = item
        r.append(biggest)
        lst_copy.remove(biggest)
    return r