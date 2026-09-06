def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if seq == []:
        return 0
    
    # Convert tuple to list if necessary for processing, but we just need to find the index
    if type(seq) == tuple:
        working_seq = list(seq)
    else:
        working_seq = seq
    
    # Find the insertion position
    for i in range(len(working_seq)):
        if working_seq[i] >= x:
            return i
    
    # If x is greater than all elements, it goes at the end
    return len(working_seq)