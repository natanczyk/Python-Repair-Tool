def top_k(lst, k):
    new_lst = []
    while lst:
        largest = lst[0]
        for num in lst:
            if num > largest:
                largest = num
        new_lst.append(largest)
        lst.remove(largest)
    return new_lst[:k]