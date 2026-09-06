def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if not seq:  # Handle empty sequence
        return 0
    enumerated = list(enumerate(seq))
    if x > seq[-1]:  # Use seq[-1] instead of max(seq) for efficiency and safety
        return len(seq)
    for i, value in enumerate(seq):
        if value >= x:
            return i