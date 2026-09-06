def top_k(lst, k):
    new_lst = []
    while lst:
        biggest = max(lst)
        lst.remove(biggest)
        new_lst.append(biggest)
    return sorted(new_lst, reverse=True)[:k]