def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    newlist = []
    while len(newlist) < k and len(temp_lst) > 0:
        max_val = max(temp_lst)
        newlist.append(max_val)
        # Find the index of the first occurrence of the maximum value
        for i in range(len(temp_lst)):
            if temp_lst[i] == max_val:
                del temp_lst[i]
                break
    return newlist