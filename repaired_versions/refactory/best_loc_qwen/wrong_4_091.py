def sort_age(lst):
    if lst == []:
        return []
    
    holder = max(lst, key=lambda x: x[1])
    lst.remove(holder)
    return [holder] + sort_age(lst)