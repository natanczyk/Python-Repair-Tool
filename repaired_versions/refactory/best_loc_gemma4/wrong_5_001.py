def top_k(lst, k):
    result = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    while k > 0:
        big = max(temp_lst)
        result.append(big)
        temp_lst.remove(big)
        k -= 1
    return result