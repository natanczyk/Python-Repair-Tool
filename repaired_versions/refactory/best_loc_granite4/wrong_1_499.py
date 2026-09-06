def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    seq = tuple(seq)
    if not seq:  # Check if the sequence is empty
        return 0
    if x > seq[-1]:  # Check if x is greater than the last element
        return len(seq)
    i = 0
    while i < len(seq):  # Iterate through the sequence
        if x <= seq[i]:
            return i
        i += 1