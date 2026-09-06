def top_k(lst, k):
    sotsot = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while len(sotsot) < k:
        m = max(temp_lst)
        sotsot.append(m)
        temp_lst.remove(m)
    return sotsot