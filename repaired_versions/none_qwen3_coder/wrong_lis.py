def lis(arr):
    if not arr:
        return 0
    
    # tails[i] stores the smallest ending element of all increasing subsequences of length i+1
    tails = []
    
    for num in arr:
        # Binary search for the position where num should be placed
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        # If num is larger than all elements in tails, append it
        if left == len(tails):
            tails.append(num)
        else:
            # Replace the element at position left
            tails[left] = num
    
    return len(tails)