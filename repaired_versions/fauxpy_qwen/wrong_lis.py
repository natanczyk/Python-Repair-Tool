import bisect

def lis(arr):
    ends = []
    longest = 0

    for val in arr:
        # Find the position to insert 'val' in 'ends'
        pos = bisect.bisect_left(ends, val)

        if pos == len(ends):
            ends.append(val)
        else:
            ends[pos] = val

        longest = max(longest, pos + 1)

    return longest