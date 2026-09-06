def top_k(lst, k):
    if k < 0 or k > len(lst):
        return []
    return sorted(lst, reverse=True)[:k]