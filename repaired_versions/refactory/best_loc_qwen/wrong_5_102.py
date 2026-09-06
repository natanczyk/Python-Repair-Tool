def top_k(lst, k):
    counter = 0
    new_lst = []
    while counter < k:
        max_val = max(lst)
        new_lst.append(max_val)
        lst.remove(max_val)
        counter += 1
    new_lst.sort(reverse=True)
    return new_lst