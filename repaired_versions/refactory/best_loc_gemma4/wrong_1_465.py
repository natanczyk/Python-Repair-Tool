def search(x, seq):
    if not seq: 
        return 0
    
    # The goal based on the test cases is to find the number of elements 
    # in the sequence that are strictly less than x.
    count = 0
    for item in seq:
        if item < x:
            count += 1
        else:
            break
    return count