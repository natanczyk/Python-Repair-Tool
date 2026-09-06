def lis(arr):
    if not arr:
        return 0
    
    ends = {}
    longest = 0

    for i, val in enumerate(arr):
        # Binary search for the position where val should be placed
        # Find the leftmost position where we can extend a subsequence
        left, right = 1, longest + 1
        pos = right
        
        while left < right:
            mid = (left + right) // 2
            if ends[mid] is not None and arr[ends[mid]] < val:
                left = mid + 1
            else:
                right = mid
        pos = left
        
        # Update the ends array
        if pos > longest:
            longest = pos
        ends[pos] = i

    return longest