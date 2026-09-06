def top_k(lst, k):
    result = []
    while len(lst) > 0 and len(result) < k:
        largest = lst[0]
        for element in lst:
            if element > largest:
                largest = element
        lst.remove(largest)
        result.append(largest)
    return result