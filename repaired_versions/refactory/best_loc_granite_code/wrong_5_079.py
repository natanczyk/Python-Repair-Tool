def top_k(lst, k):
    # Fill in your code here
    sort_lst = []
    while lst: # a is not []
        largest = lst[0]
        for element in lst:
            if element > largest:
                largest = element
        lst.remove(largest)
        sort_lst.append(largest)
    return sort_lst[:k]