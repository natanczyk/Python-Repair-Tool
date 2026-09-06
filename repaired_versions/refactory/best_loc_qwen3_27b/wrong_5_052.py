def top_k(lst, k):
    # Implement a simple sorting algorithm (e.g., bubble sort) in descending order
    # since we cannot use sort() or sorted()
    arr = lst[:]  # Make a copy to avoid modifying the original list
    n = len(arr)
    
    # Bubble sort in descending order
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr[0:k]