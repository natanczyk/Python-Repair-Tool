def top_k(lst, k):
    if k == 0:
        return []
    
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    sort = []
    # Selection sort to sort the list in ascending order
    while temp_lst:
        smallest = temp_lst[0]
        for i in temp_lst:
            if i < smallest:
                smallest = i
        temp_lst.remove(smallest)
        sort.append(smallest)
    
    # The 'sort' list is now in ascending order.
    # To get the top k greatest values in descending order, 
    # we slice the last k elements and reverse them.
    result = sort[len(sort)-k:]
    # Reverse the slice to get descending order
    return result[::-1]