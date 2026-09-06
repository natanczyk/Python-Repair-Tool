def top_k(lst, k):
    counter = 0
    new_lst = []
    lst = lst.copy()  # Avoid modifying the original list
    while counter < k:
        maxi = max(lst)
        new_lst.append(maxi)
        lst.remove(maxi)
        counter += 1
    return new_lst