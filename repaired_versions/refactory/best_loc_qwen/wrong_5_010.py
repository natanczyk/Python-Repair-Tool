def top_k(lst, k):
    n = len(lst) - k
    counter = 0
    while counter < n:
        lst.remove(min(lst))
        counter = counter + 1
    sort_list = sorted(lst, reverse=True)
    return sort_list