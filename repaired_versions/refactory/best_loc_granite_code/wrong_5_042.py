def top_k(lst, k):
    #top k in descending order
    sort = []
    x = len(lst)
    if k > x:
        raise ValueError("k cannot be greater than the length of the list")
    while x > 0 and k > 0:
        largest = lst[0]
        for element in lst:
            if element > largest:
                largest = element
        lst.remove(largest)
        sort.append(largest)
        x -= 1
        k -= 1
    return sort