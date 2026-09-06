def sort_age(lst):
    if not lst:
        return []

    youngest = lst[0][1]
    for item in lst:
        if item[1] < youngest:
            youngest = item[1]
    
    lst.sort(key=lambda x: x[1], reverse=True)
    return lst