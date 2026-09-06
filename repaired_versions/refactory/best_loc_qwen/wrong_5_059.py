def top_k(lst, k):
    new_lst = []
    while k > 0:
        max_val = max(lst)
        lst.remove(max_val)
        new_lst.append(max_val)
        k -= 1
    return sorted(new_lst, reverse=True)