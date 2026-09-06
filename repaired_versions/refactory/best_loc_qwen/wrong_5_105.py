def top_k(lst, k):
    sort = []
    while lst:
        largest = lst[0]
        for element in lst:
            if element > largest:
                largest = element
        lst.remove(largest)
        sort.append(largest)
    return sorted(sort, reverse=True)[:k]