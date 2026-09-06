def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if not seq:  # Check if the sequence is empty
        return 0
    if x < seq[0]:
        return 0
    if x > seq[-1]:
        return len(seq)
    for i in range(len(seq)):
        if seq[i] >= x:
            return i
    return len(seq)  # In case x is greater than all elements (should not happen due to previous check)