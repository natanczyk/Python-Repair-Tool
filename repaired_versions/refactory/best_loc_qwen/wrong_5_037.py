def top_k(lst, k):
    sort = []
    while lst:
        smallest = lst[0]
        for i in lst:
            if i < smallest:
                smallest = i
        lst.remove(smallest)
        sort.append(smallest)
    sort.sort(reverse=True)
    return sort[:k]