def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if not seq:  # Check if the sequence is empty
        return 0
    elif x > seq[-1]:  # Use seq[-1] to get the last element, more efficient than max(seq)
        return len(seq)
    else:
        for i, value in enumerate(seq):
            if value >= x:
                return i