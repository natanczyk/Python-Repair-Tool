def top_k(lst, k):
    if k <= 0:
        return []
    else:
        maxi = max(lst)
        new_list = lst.copy()
        new_list.remove(maxi)  # Use remove to eliminate the first occurrence of maxi
        return [maxi] + top_k(new_list, k - 1)