def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if seq == []:
        return 0
    
    # To maintain sorted order and pass tests like test_case012 (search(5, [5, 5, 5]) == 0)
    # and test_case014 (search(1, [1]) == 0), we need to find the FIRST index i 
    # where seq[i] >= x.
    for i in range(len(seq)):
        if seq[i] >= x:
            return i
            
    return len(seq)