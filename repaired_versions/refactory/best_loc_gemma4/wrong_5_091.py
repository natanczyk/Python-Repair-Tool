def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    arr = list(lst)
    n = len(arr)
    
    # Implement Bubble Sort to sort the list in descending order
    # Since we are not allowed to use sort() or sorted()
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    # Return the first k elements of the sorted list
    return arr[:k]