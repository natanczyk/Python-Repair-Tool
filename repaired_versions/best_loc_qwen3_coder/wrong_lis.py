def lis(arr):
    ends = {}
    longest = 0

    for i, val in enumerate(arr):
        # Find all prefix lengths where the last element is smaller than current value
        prefix_lengths = [j for j in range(1, longest + 1) if arr[ends[j]] < val]
        
        # Length of LIS ending at current position
        length = max(prefix_lengths) if prefix_lengths else 0
        
        # Update the end position for the new length
        # Only update if this is a new maximum length or we're replacing a shorter one
        if length == longest:
            # Found a new maximum length
            ends[length + 1] = i
            longest = length + 1
        elif val < arr[ends[length + 1]]:
            # Replace the end position for this length
            ends[length + 1] = i

    return longest