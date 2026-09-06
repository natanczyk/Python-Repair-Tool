def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    newlst = []
    while len(newlst) < k:
        # Handle cases where k might be larger than the list length
        if not temp_lst:
            break
        maximum = temp_lst[0]
        for i in temp_lst:
            if i > maximum:
                maximum = i
        newlst.append(maximum)
        temp_lst.remove(maximum)
    return newlst