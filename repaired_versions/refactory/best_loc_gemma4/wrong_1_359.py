def search(x, seq):
    if not seq:
        return 0
    if x <= seq[0]:
        return 0
    
    # To satisfy test_case007: search(10, (-5, -1, 3, 5, 7, 10)) == 5
    # The target x=10 is the last element. The expected result 5 is the index of the last element.
    # This implies the function should return the index i such that seq[i-1] < x <= seq[i] 
    # or similar logic where the boundary is handled specifically.
    
    for i in range(0, len(seq)):
        if x <= seq[i]:
            return i
            
    return len(seq)