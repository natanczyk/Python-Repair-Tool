def search(x, seq):
    if not seq:
        return 0
    
    # The goal is to find the index of the first element in the sequence 
    # that is greater than or equal to x.
    # Based on the test cases:
    # search(10, (-5, -1, 3, 5, 7, 10)) == 5 (index of 10)
    # search(5, [5, 5, 5]) == 0 (index of first 5)
    # search(1, [1]) == 0 (index of 1)
    
    for i in range(len(seq)):
        if seq[i] >= x:
            return i
            
    return len(seq)