def top_k(lst, k):
    new_lst = []
    while lst and len(new_lst) < k:
        largest = lst[0]
        largest_index = 0
        for index, numbers in enumerate(lst):
            if numbers > largest:
                largest = numbers
                largest_index = index
        new_lst.append(lst.pop(largest_index))
    return new_lst