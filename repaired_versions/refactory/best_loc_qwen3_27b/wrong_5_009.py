def top_k(lst, k):
    n = len(lst)
    # Remove the n - k smallest elements to keep the top k
    counter = 0
    while counter < n - k:
        lst.remove(min(lst))
        counter = counter + 1
    sort_list = []
    while lst != []:
        sort_list.append(max(lst))
        lst.remove(max(lst))
    return sort_list