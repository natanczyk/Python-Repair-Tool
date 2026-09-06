def sort_age(lst):
    if not lst:
        return []
    max_elem = max(lst, key=lambda x: x[1])
    max_index = lst.index(max_elem)
    return [max_elem] + sort_age(lst[:max_index] + lst[max_index+1:])