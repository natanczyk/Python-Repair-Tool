def top_k(lst, k):
    # Create a copy of the list to avoid mutating the original input
    temp_lst = list(lst)
    sort = []
    while temp_lst:
        largest = temp_lst[0]
        for element in temp_lst:
            if element > largest:
                largest = element
        temp_lst.remove(largest)
        sort.append(largest)
    return sort[0:k]