def top_k(lst, k):
    results = []
    counter = 0
    while counter < k:
        max_value = float('-inf')
        max_index = -1
        for i in range(len(lst)):
            if lst[i] > max_value:
                max_value = lst[i]
                max_index = i
        if max_index != -1:
            results.append(lst.pop(max_index))
            counter += 1
    return results