def top_k(lst, k):
    # Create a copy of the list to avoid mutating the original input
    temp_lst = list(lst)
    sort = []
    while temp_lst: 
        biggest = temp_lst[0]
        for element in temp_lst:
            if element > biggest:
                biggest = element
        temp_lst.remove(biggest)
        sort.append(biggest)
    return sort[:k]