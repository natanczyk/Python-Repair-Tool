def search(x, seq):
    if not seq:  # Check if the sequence is empty
        return 0
    
    for i, elem in enumerate(seq):
        if x <= elem:
            return i
        elif x > seq[-1]:  # Directly compare with the last element
            return len(seq)
        
    # This line should theoretically never be reached due to the checks above
    return len(seq)
    
    """ Takes in a value x and a sorted sequence seq, and returns the
    position that x should go to such that the sequence remains sorted """