def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    arr = list(lst)
    n = len(arr)
    # Bubble sort to sort the list in ascending order
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Correct swap logic using tuple unpacking
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    # Reverse the sorted list to get descending order
    arr.reverse()
    
    # Return the first k elements
    return arr[:k]