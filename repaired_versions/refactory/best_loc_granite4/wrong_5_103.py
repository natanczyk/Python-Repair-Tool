def top_k(lst, k):
    new_lst = []
    while k > 0:
        maxi = max(lst)
        new_lst.append(maxi)
        lst.remove(maxi)
        k -= 1
    return new_lst