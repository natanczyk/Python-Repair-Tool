def top_k(lst, k):
    # Make a copy to avoid modifying the original list
    arr = lst[:]
    n = len(arr)
    
    # Perform a full bubble sort in descending order
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr[:k]