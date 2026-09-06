def top_k(lst, k):
    lst_res = lst.copy()  # Create a copy to avoid mutating the original list
    sort = []
    while lst_res and len(sort) < k:
        largest = lst_res[0]
        for element in lst_res:  # Use singular 'element' to match the loop variable
            if element > largest:
                largest = element
        lst_res.remove(largest)
        sort.append(largest)
    return sort