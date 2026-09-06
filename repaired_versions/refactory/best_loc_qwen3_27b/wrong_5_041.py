def top_k(lst, k):
    # Make a copy to avoid modifying the original list
    arr = lst[:]
    
    # Implement a simple sorting algorithm (e.g., bubble sort or selection sort)
    # We'll use selection sort to sort in descending order
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    
    # Return the top k elements
    return arr[:k]