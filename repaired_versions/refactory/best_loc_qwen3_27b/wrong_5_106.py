def top_k(lst, k):
    new = []
    # Sort in descending order to get largest elements first
    # We cannot use sorted() or .sort() directly per constraints, but we can implement our own sort
    # Let's implement a simple selection sort or bubble sort for descending order
    
    # Create a copy to avoid modifying original list
    arr = lst[:]
    
    # Bubble sort in descending order
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    # Take the first k elements (which are the largest, in descending order)
    for i in range(k):
        new.append(arr[i])
    
    return new