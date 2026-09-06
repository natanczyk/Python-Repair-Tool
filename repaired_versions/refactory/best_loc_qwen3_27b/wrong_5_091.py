def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original
    lst_copy = lst[:]
    
    # Sort the list in descending order using a simple sorting algorithm (e.g., selection sort)
    # Since we can't use sort() or sorted(), we'll implement our own sorting
    
    # Selection sort in descending order
    n = len(lst_copy)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if lst_copy[j] > lst_copy[max_idx]:
                max_idx = j
        lst_copy[i], lst_copy[max_idx] = lst_copy[max_idx], lst_copy[i]
    
    # Return the top k elements
    return lst_copy[:k]