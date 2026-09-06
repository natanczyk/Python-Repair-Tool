def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):
        # Find the position to insert val in ends using binary search
        low, high = 0, longest
        while low < high:
            mid = (low + high) // 2
            if arr[ends[mid]] < val:
                low = mid + 1
            else:
                high = mid
        
        # If val is larger than all elements in ends, extend the longest subsequence
        if low == longest:
            longest += 1
        ends[low] = i

    return longest