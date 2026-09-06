def top_k(lst, k):
    sotsot = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while len(sotsot) < k and temp_lst:
        max_val = max(temp_lst)
        sotsot.append(max_val)
        temp_lst.remove(max_val)
    return sotsot