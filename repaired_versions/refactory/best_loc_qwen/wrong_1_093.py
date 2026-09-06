def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if not seq:  # Check if the sequence is empty
        return 0
    
    if x <= seq[0]:
        return 0
    if x > seq[-1]:
        return len(seq)
    else:
        for i, elem in enumerate(seq):
            if x > elem and (i + 1 < len(seq) and x <= seq[i + 1]):
                return i + 1