def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """
    if not seq:  # Handles both empty list and empty tuple
        return 0
    if x < seq[0]:
        return 0
    if x > seq[-1]:  # Use -1 index for last element
        return len(seq)
    for i in range(len(seq)):  # Iterate through all elements
        if seq[i] >= x:  # Find the first position where x should be inserted
            return i