def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    new_lst = []
    while temp_lst:
        largest_idx = 0
        for i in range(1, len(temp_lst)):
            if temp_lst[i] > temp_lst[largest_idx]:
                largest_idx = i
        new_lst.append(temp_lst.pop(largest_idx))
    return new_lst[:k]