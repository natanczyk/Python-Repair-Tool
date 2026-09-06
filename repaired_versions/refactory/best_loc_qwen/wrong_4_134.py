def sort_age(lst):
    if lst == []:
        return []
    else:
        largest = max(lst, key=lambda x: x[1])
        lst.remove(largest)
        return [largest] + sort_age(lst)