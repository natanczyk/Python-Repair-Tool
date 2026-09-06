def sort_age(lst):
    if not lst:
        return []
    return sorted(lst, key=lambda x: x[1], reverse=True)