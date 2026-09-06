def top_k(lst, k):
    new_list = []
    for i in range(k):
        if not lst:
            break
        new_list.append(max(lst))
        lst.remove(max(lst))
    return new_list