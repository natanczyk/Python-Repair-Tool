def top_k(lst, k):
    i = 0
    while i < len(lst):
        max_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] > lst[max_index]:
                max_index = j
        lst[i], lst[max_index] = lst[max_index], lst[i]
        i += 1
    
    return lst[:k] if k <= len(lst) else lst