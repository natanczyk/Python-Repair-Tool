def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    new_lst = []
    while temp_lst:
        biggest = temp_lst[0]
        for x in temp_lst:
            if x > biggest:
                biggest = x
        temp_lst.remove(biggest)
        new_lst.append(biggest)
    return new_lst[0:k]