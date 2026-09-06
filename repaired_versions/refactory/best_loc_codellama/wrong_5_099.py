def top_k(lst, k):
    if k < 1 or k > len(lst):
        return []
    return sorted(lst, reverse=True)[:k]