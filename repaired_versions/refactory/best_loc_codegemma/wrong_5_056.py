def top_k(lst, k):
    values = []
    while len(values) < k:
        greatest = lst[0]
        for item in lst:
            if item > greatest:
                greatest = item
        values.append(greatest)
        lst.remove(greatest)
        
    return values