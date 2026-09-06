def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    # The goal is to find the index where x should be inserted to maintain order.
    # Since the sequence is already sorted, we just need to find the first element 
    # that is greater than or equal to x.
    
    for i in range(len(seq)):
        if seq[i] >= x:
            return i
            
    # If the loop finishes without returning, it means x is greater than all 
    # elements in the sequence (or the sequence is empty), so it goes at the end.
    return len(seq)