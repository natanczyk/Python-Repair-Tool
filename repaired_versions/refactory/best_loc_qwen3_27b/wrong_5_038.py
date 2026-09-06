def top_k(lst, k):
    # Make a copy to avoid modifying the original list
    arr = lst[:]
    
    # Implement bubble sort to sort in descending order
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    # Return the top k elements
    return arr[:k]