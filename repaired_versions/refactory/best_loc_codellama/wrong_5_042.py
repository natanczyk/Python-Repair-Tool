def top_k(lst, k):
    # top k in descending order
    sort = []
    x = len(lst)
    while x > 0:
        largest = lst[0]
        for element in lst:
            if element > largest:
                largest = element
        lst.remove(largest)
        sort.append(largest)
        x -= 1
    return sort[:k]