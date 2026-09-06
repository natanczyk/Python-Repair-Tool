def search(x, seq): 
    # The goal is to find the index where x should be inserted to maintain 
    # sorted order, or the index of the first occurrence of x.
    # This is equivalent to finding the number of elements in seq that are strictly less than x.
    
    count = 0
    for item in seq:
        if item < x:
            count += 1
        else:
            break
    return count