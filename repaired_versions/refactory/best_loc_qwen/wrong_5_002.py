def top_k(lst, k):
    lst_res = lst[:]  # Create a shallow copy of the list
    sort = []
    while len(sort) < k:
        largest = lst_res[0]
        for element in lst_res:  # Corrected from 'elements' to 'element'
            if element > largest:
                largest = element
        lst_res.remove(largest)
        sort.append(largest)
    return sort