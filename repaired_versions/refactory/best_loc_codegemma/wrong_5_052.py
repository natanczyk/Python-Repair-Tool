def top_k(lst, k):
    lst.sort(reverse=True)
    return lst[:k]