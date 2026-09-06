def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    temp_lst = list(lst)
    new_lst = []
    while temp_lst:
        largest = temp_lst[0]
        for number in temp_lst:
            if number > largest:
                largest = number
        new_lst.append(largest)
        temp_lst.remove(largest)
    return new_lst[:k]