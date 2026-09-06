def top_k(lst, k):
    # Implementing a simple selection sort to sort the list in descending order
    for i in range(len(lst)):
        max_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] > lst[max_idx]:
                max_idx = j
        lst[i], lst[max_idx] = lst[max_idx], lst[i]
    
    # Return the top k elements
    return lst[:k]