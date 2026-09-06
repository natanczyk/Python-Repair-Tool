def top_k(lst, k):
    n = len(lst)
    for i in range(k):
        max_idx = i
        for j in range(i + 1, n):
            if lst[j] > lst[max_idx]:
                max_idx = j
        lst[i], lst[max_idx] = lst[max_idx], lst[i]
    return lst[:k]