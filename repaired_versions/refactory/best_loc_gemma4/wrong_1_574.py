def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if seq == [] or seq == ():
        return 0
    if x < seq[0]:
        return 0
    elif x > seq[len(seq)-1]:
        return len(seq)
    else:
        for i in range(len(seq)):
            if seq[i] == x:
                return i
            elif i < len(seq) - 1 and seq[i] < x < seq[i+1]:
                return i + 1
        # This part handles the case where x is equal to the last element 
        # but the loop logic needs to be robust.
        return len(seq)