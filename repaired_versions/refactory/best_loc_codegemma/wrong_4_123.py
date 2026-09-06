def sort_age(lst):
    if not lst:
        return []
    result = sorted(lst, key=lambda x: x[1], reverse=True)
    return result