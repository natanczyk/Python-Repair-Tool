def search(x, seq):
    if not seq:
        return 0
    
    # The goal of this search function, based on the test cases, 
    # is to find the index of the first element that is greater than or equal to x.
    # If x is greater than all elements, it returns the length of the sequence.
    
    for i, element in enumerate(seq):
        if x <= element:
            return i
            
    return len(seq)