def lis(arr):
    if not arr:
        return 0
    
    # ends[i] stores the index of the smallest tail element of all increasing subsequences of length i+1
    # We use a list where ends[k] is the smallest ending value of an increasing subsequence of length k+1
    tails = []
    
    for val in arr:
        # Binary search for the position where val should be inserted
        left, right = 0, len(tails)
        while left < right:
            mid = (left + right) // 2
            if tails[mid] < val:
                left = mid + 1
            else:
                right = mid
        
        if left == len(tails):
            tails.append(val)
        else:
            tails[left] = val
    
    return len(tails)