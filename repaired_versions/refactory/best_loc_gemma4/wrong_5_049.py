def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    sorted_lst = []
    while temp_lst:
        biggest = temp_lst[0]
        for n in temp_lst:
            if n >= biggest:
                biggest = n
        temp_lst.remove(biggest)
        sorted_lst.append(biggest)
    return sorted_lst[0:k]