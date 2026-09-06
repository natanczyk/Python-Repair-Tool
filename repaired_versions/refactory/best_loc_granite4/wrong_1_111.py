def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if not seq:  # Handle empty sequence
        return 0
    if x < seq[0]:  # Handle case where x is smaller than the first element
        return 0
    for i in range(len(seq) - 1):
        if x > seq[i] and x <= seq[i + 1]:
            return i + 1
    if x > seq[-1]:  # Handle case where x is larger than the last element
        return len(seq)
    return 0  # If x is equal to an element, return the first occurrence index