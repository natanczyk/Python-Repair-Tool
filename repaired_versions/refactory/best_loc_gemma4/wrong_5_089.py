def top_k(lst, k):
    newlist = []
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    while temp_lst and len(newlist) < k:
        biggest = temp_lst[0]
        for i in temp_lst:
            if i > biggest:
                biggest = i
        temp_lst.remove(biggest)
        newlist.append(biggest)
    return newlist