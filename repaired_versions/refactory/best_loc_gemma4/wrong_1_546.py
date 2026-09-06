def search(x, seq):
    if not seq:
        return 0
    
    # The test cases indicate that the function should return the index 
    # of the first element in the sorted sequence that is greater than or equal to x.
    # This is equivalent to bisect_left in Python's bisect module.
    
    low = 0
    high = len(seq)
    while low < high:
        mid = (low + high) // 2
        if seq[mid] < x:
            low = mid + 1
        else:
            high = mid
    return low