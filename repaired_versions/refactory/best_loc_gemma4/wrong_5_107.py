def top_k(lst, k):

    newlst = []
    # Create a copy of the list to avoid modifying the original input list
    temp_lst = list(lst)
    for i in range(k):
        # Find the maximum value in the current list
        max_val = max(temp_lst)
        newlst.append(max_val)
        # Remove only one instance of the maximum value
        temp_lst.remove(max_val)
    return newlst