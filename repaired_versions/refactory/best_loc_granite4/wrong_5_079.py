def top_k(lst, k):
    sort_lst = []
    while lst:  # lst is not empty
        largest = lst[0]
        for element in lst:
            if element > largest:
                largest = element
        lst.remove(largest)
        sort_lst.append(largest)
    return sort_lst[:k]