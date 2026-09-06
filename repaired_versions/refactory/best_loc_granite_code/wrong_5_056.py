def top_k(lst, k):
    values = []
    while len(values) < k:
        greatest = float('-inf')
        for item in lst:
            if item > greatest:
                greatest = item
        lst.remove(greatest)
        values.append(greatest)
        
    return values