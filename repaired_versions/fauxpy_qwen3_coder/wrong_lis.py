def lis(arr):
    if not arr:
        return 0
    
    # ends[i] stores the smallest ending element of all increasing subsequences of length i+1
    ends = []
    
    for val in arr:
        # Binary search for the position where val should be placed
        left, right = 0, len(ends)
        while left < right:
            mid = (left + right) // 2
            if ends[mid] < val:
                left = mid + 1
            else:
                right = mid
        
        # If val is larger than all elements in ends, append it
        if left == len(ends):
            ends.append(val)
        else:
            # Replace the element at position left
            ends[left] = val
    
    return len(ends)