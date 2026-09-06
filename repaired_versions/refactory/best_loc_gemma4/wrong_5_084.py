def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    arr = list(lst)
    
    # Implement a simple Bubble Sort to sort the list in descending order
    # since sorted() and .sort() are forbidden.
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    # Return the first k elements of the sorted list
    return arr[:k]