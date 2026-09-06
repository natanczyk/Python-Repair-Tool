def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original input
    nums = list(lst)
    # Implement a simple bubble sort to sort the list in descending order
    # since sorted() and .sort() are forbidden.
    n = len(nums)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    
    # Return the first k elements of the sorted list
    return nums[:k]