def top_k(lst, k):
    sort = sorted(lst, reverse=True)
    output = sort[:k]
    return output