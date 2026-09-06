def top_k(lst, k):
    sort = []
    while lst:
        smallest = lst[0]
        for i in lst:
            if i < smallest:
                smallest = i
        lst.remove(smallest)
        sort.append(smallest)
    
    # sort is now sorted in ascending order
    # We want the top k elements in descending order
    # The largest elements are at the end of 'sort'
    # Take the last k elements and reverse them to get descending order
    result = sort[-k:] if k > 0 else []
    result.reverse()
    return result