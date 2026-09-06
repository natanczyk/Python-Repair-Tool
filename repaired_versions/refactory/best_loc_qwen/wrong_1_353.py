def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    # Check if the sequence is empty before entering the loop
    if seq == () or seq == []:
        return 0
    
    largest = seq[0]
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
    return len(seq)