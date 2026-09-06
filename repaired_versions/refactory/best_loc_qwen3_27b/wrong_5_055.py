def top_k(lst, k):
    values = []
    lst = lst.copy()  # Avoid modifying the original list
    while len(values) < k:
        if not lst:
            break
        greatest = lst[0]
        for item in lst:
            if item > greatest:
                greatest = item
        lst.remove(greatest)
        values.append(greatest)
    return values