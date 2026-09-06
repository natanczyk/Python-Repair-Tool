def top_k(lst, k):
    # Implementing a simple selection sort to sort the list in descending order
    n = len(lst)
    for i in range(n):
        # Find the maximum element in the remaining unsorted portion
        max_idx = i
        for j in range(i + 1, n):
            if lst[j] > lst[max_idx]:
                max_idx = j
        # Swap the found maximum element with the first element of the unsorted portion
        lst[i], lst[max_idx] = lst[max_idx], lst[i]
    
    # Return the top k elements
    return lst[:k]