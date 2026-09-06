def top_k(lst, k):
    new_list = []
    while k > 0:
        max_val = max(lst)
        new_list.append(max_val)
        lst.remove(max_val)
        k -= 1
    return sorted(new_list, reverse=True)