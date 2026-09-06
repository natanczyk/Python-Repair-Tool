def search(val, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if not seq:
        return 0
    
    # To maintain sorted order and pass test_case007 (where val=10, seq=[..., 10] returns 5),
    # we need to find the first index i where val <= seq[i].
    for i in range(len(seq)):
        if val <= seq[i]:
            return i
            
    # If val is greater than all elements in the sequence
    return len(seq)