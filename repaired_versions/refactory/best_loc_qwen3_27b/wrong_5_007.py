def top_k(lst, k):
    # Handle edge case where k is 0 or list is empty
    if k <= 0 or not lst:
        return []
    
    # Create a copy of the list to work with
    lst1 = lst[:]
    
    # Sort the list in descending order using selection sort
    sort = []
    while lst1 and len(sort) < k:
        biggest = lst1[0]
        for element in lst1:
            if element > biggest:
                biggest = element
        lst1.remove(biggest)
        sort.append(biggest)
    
    return sort