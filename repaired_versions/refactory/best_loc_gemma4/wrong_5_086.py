def top_k(lst, k):
    # Create a copy of the list to avoid mutating the original input
    temp_lst = list(lst)
    result = []
    while len(result) < k:
        a = max(temp_lst)
        temp_lst.remove(a)
        result.append(a)
    return result