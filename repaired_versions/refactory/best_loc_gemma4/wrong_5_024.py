def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    sort = []
    while temp_lst:
        biggest = temp_lst[0]
        for i in temp_lst[1:]:
            if i > biggest:
                biggest = i
        # Remove the first occurrence of the biggest element found
        temp_lst.remove(biggest)
        sort.append(biggest)
    
    # The 'sort' list is already in descending order because we extracted the max repeatedly
    sort_k = []
    n = 0
    while n < k and n < len(sort):
        sort_k.append(sort[n])
        n += 1
    
    return sort_k