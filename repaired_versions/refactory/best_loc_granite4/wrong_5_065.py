def top_k(lst, k):
    # Create a copy of the list to avoid modifying the original
    nums = lst[:]
    result = []
    
    for _ in range(k):
        if not nums:  # If the list is empty, break out of the loop
            break
        # Find the maximum value in the list
        max_val = nums[0]
        for num in nums:
            if num > max_val:
                max_val = num
        result.append(max_val)
        # Remove the found maximum value from the list
        nums.remove(max_val)
    
    return result