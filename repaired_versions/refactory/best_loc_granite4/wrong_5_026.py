def top_k(lst, k):
    if not lst:
        return []
    result = []
    while lst and len(result) < k:
        largest = lst[0]
        for i in lst:
            if i > largest:
                largest = i
        lst.remove(largest)
        result.append(largest)
    return result