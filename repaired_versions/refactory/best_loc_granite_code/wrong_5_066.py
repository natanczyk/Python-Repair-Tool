def top_k(lst, k):
    # Fill in your code here
    a = lst
    sort = []
    while a:
        largest = max(a)
        a.remove(largest)
        sort.append(largest)
    return(sort)[:k]