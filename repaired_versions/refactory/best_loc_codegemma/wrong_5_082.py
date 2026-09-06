def top_k(lst, k):
    sotsot = []
    while lst:
        max_num = max(lst)
        sotsot.append(max_num)
        lst.remove(max_num)
    return sotsot[:k]