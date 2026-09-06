def top_k(lst, k):
    # Create a copy of the input list to avoid modifying the original list
    temp_lst = list(lst)
    result = []
    # Collect the maximum element k times
    while len(result) < k and len(temp_lst) > 0:
        a = max(temp_lst)
        temp_lst.remove(a)
        result.append(a)
    return result