def sort_age(lst):
    if not lst:
        return []
    
    sort1 = sorted(lst, key=lambda x: x[1], reverse=True)
    return sort1