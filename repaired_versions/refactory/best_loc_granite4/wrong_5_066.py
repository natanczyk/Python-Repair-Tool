def top_k(lst, k):
    a = lst[:]
    result = []
    while a and len(result) < k:
        largest = a[0]
        for item in a:
            if item > largest:
                largest = item
        a.remove(largest)
        result.append(largest)
    return result