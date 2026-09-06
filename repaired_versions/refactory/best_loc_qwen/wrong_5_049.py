def top_k(lst, k):
    sorted_lst = []
    while lst and k > 0:
        biggest = lst[0]
        for n in lst:
            if n >= biggest:
                biggest = n
        lst.remove(biggest)
        sorted_lst.append(biggest)
        k -= 1
    return sorted_lst