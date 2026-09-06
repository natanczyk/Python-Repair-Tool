def top_k(lst, k):
    sorted_list = sorted(lst, reverse=True)
    return sorted_list[:k]