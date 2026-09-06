def top_k(lst, k):
    if k <= 0:
        return []
    elif k >= len(lst):
        return sorted(lst, reverse=True)
    else:
        maxi = max(lst)
        pos = lst.index(maxi)
        new_list = lst.copy()
        new_list.pop(pos)
        return [maxi] + top_k(new_list, k - 1)