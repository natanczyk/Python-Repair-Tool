def search(x, seq):
    # Handle empty sequence
    if len(seq) == 0:
        return 0
    
    # If x is less than or equal to the first element, insert at position 0
    if x <= seq[0]:
        return 0
    
    # If x is greater than the last element, insert at the end
    if x > seq[len(seq) - 1]:
        return len(seq)
    
    # Search for the position where x fits
    for i in range(len(seq) - 1):
        if seq[i] < x <= seq[i + 1]:
            return i + 1
    
    # If x equals the last element or falls between last-1 and last
    # This handles cases where x == seq[i] for some i
    for i in range(len(seq)):
        if x == seq[i]:
            return i