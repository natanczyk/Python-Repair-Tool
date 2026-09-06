def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if not seq:  # Check for any empty sequence (list or tuple)
        return 0
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
    return len(seq)  # Return the length of seq if x is greater than all elements