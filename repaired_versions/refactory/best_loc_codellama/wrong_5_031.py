def top_k(lst, k):
    new_lst = []
    while lst:
        largest = lst[0]
        for i in range(1, len(lst)):
            if lst[i] > largest:
                largest = lst[i]
        new_lst.append(largest)
        lst.remove(largest)
    return new_lst[:k]