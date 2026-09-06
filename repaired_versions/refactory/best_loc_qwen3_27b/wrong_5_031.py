def top_k(lst, k):
    new_lst = []
    while lst:
        largest = lst[0] 
        largest_index = 0
        for i in range(1, len(lst)):
            if lst[i] > largest:
                largest = lst[i]
                largest_index = i
        new_lst.append(lst.pop(largest_index))
    return new_lst[:k]